# src/fastsocket/event_registry.py

import importlib
import inspect
import os
from typing import Callable, Any, get_type_hints, Optional

import inflection
import reactivex as rx
from loguru import logger
from pydantic import BaseModel, ValidationError

from fastsocket.logger import info, warning, debug, error

# Dictionary to store event subjects
event_subjects = {}


def validate_data(func: Callable, data: Any) -> Any:
    type_hints = get_type_hints(func)
    model = type_hints.get('data', None)

    if model and issubclass(model, BaseModel):
        try:
            # Validate data using the Pydantic model
            debug(f"Validating data for function '{func.__name__}' with model '{model.__name__}'")
            return model(**data)
        except ValidationError as e:
            error(f"Validation error for function '{func.__name__}': {e.errors()}")
            return e.errors()
    return data


def create_event_wrapper(event_name: str, func: Callable) -> Callable:
    if event_name not in event_subjects:
        event_subjects[event_name] = rx.Subject()

    from fastsocket import sio

    async def wrapper(sid: str, data: Any, *args, **kwargs) -> Any:
        info(f"Handling event '{event_name}' from sid '{sid}' with data: {data}")

        # Validate data
        validated_data_or_error = validate_data(func, data)

        # If validation fails, emit an error and return early
        if isinstance(validated_data_or_error, list):
            await sio.emit("error", {"error": validated_data_or_error}, room=sid)
            error(f"Validation failed for event '{event_name}' with errors: {validated_data_or_error}")
            return

        validated_data = validated_data_or_error

        # Define the `ack` function to send a default or custom acknowledgment
        async def ack(response_data: Optional[dict] = None):
            """
            Acknowledgment function to emit a success message to the client with defaults.

            Args:
                response_data (Optional[Dict]): Optional custom payload for acknowledgment.
            """
            # Default payload for acknowledgment
            default_payload = {
                "status": "success",
                "message": "Operation successful"
            }

            # Use provided response_data to override defaults if given
            payload = {**default_payload, **(response_data or {})}

            ack_name = f"{event_name}_ack"  # Acknowledge event based on handler name
            logger.info(f"Emitting acknowledgment '{ack_name}' for SID '{sid}' with data: {payload}")
            await sio.emit(ack_name, payload, room=sid)

        # Create and populate the 'injectable' dictionary
        injectable = {
            'sid': sid,
            'event_name': event_name,
            'sio': sio,
            'logger': logger,
            'data': validated_data,
            'ack': ack
        }

        # Filter injectable parameters based on function signature
        func_signature = inspect.signature(func)
        filtered_injectable = {k: v for k, v in injectable.items() if k in func_signature.parameters}

        # Call the original function with filtered 'injectable'
        debug(
            f"Calling function '{func.__name__}' for event '{event_name}' with injectable: {filtered_injectable}")
        return await func(*args, **kwargs, **filtered_injectable)

    # Register the wrapper function as an event handler with Socket.IO
    sio.on(event_name, wrapper)
    info(f"Registered event '{event_name}' with function '{func.__name__}'")


def register_event_handler(module_name: str, func: Callable) -> None:
    # Convert the snake_case module name to camelCase for the event name
    event_name = inflection.camelize(module_name, uppercase_first_letter=False)
    debug(f"Registering event handler for module '{module_name}' as event '{event_name}'")
    create_event_wrapper(event_name, func)


async def register_events(event_directory: str = "src/fastsocket/events", reload: bool = False):
    """Register or reload event handlers from a directory."""
    info(f"Registering events from directory '{event_directory}' (reload={reload})")
    for filename in os.listdir(event_directory):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            module_path = f"fastsocket.events.{module_name}"
            debug(f"Loading module '{module_name}' from '{event_directory}'")

            try:
                # Reload the module if reload is True
                module = importlib.import_module(module_path)
                if reload:
                    module = importlib.reload(module)
            except Exception as e:
                error(f"Failed to load or reload module '{module_name}': {str(e)}")
                continue

            # Look for a function named 'handle_event' in the module
            if hasattr(module, 'handle_event'):
                handle_event_func = getattr(module, 'handle_event')
                if callable(handle_event_func) and inspect.iscoroutinefunction(handle_event_func):
                    debug(f"Found 'handle_event' function in module '{module_name}'")
                    # Register the 'handle_event' function for the module with converted event name
                    register_event_handler(module_name, handle_event_func)
                else:
                    warning(f"'handle_event' in module '{module_name}' is not a coroutine function")
            else:
                warning(f"No 'handle_event' function found in module '{module_name}'")
