# src/fastsocket/cli.py
import httpx
import typer
import subprocess
import os
import sys
import signal
import time
from pathlib import Path
from typing import Optional, List
import importlib
import inspect
from loguru import logger

from fastsocket.logger import info, error, success, warning
from .event_registry import register_events
from fastsocket import socket_app
from fastsocket.commands.asyncapi_cmds import app as asyncapi_cmds_app
from fastsocket.commands.log_cmds import app as log_cmds_app

# Initialize Typer app
app = typer.Typer()

app.add_typer(log_cmds_app, name="log", help="Manage log files and view logs.")
app.add_typer(asyncapi_cmds_app, name="asyncapi", help="Manage AsyncAPI files and generate documentation.")

# Constants
PID_FILE = Path("fastsocket.pid")
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 8000
EVENTS_DEFAULT_DIR = "./events"


def is_server_running() -> bool:
    if PID_FILE.exists():
        try:
            pid = int(PID_FILE.read_text())
            os.kill(pid, 0)
            return True
        except (OSError, ValueError):
            return False
    return False


def get_server_pid() -> Optional[int]:
    if PID_FILE.exists():
        try:
            pid = int(PID_FILE.read_text())
            return pid
        except ValueError:
            return None
    return None


def write_pid(pid: int):
    PID_FILE.write_text(str(pid))


def remove_pid():
    if PID_FILE.exists():
        PID_FILE.unlink()


@app.command()
def register_events_command(directory: str = EVENTS_DEFAULT_DIR):
    """
    Register event handlers from a specified directory.
    """
    info(f"Registering events from directory '{directory}'")
    try:
        register_events(event_directory=directory)
        success(f"Successfully registered events from '{directory}'")
    except Exception as e:
        error(f"Failed to register events: {e}")
        raise typer.Exit(code=1)


@app.command()
def start(host: str = DEFAULT_HOST, port: int = DEFAULT_PORT):
    """
    Start the FastSocket server.
    """
    if is_server_running():
        error("FastSocket server is already running.")
        raise typer.Exit(code=1)

    info(f"Starting FastSocket server on {host}:{port}")

    # Start the server as a subprocess
    # Using 'uvicorn' to run the 'socket_app' from 'api.py'
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "fastsocket.api:socket_app", "--host", host, "--port", str(port)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Write the PID to the PID file
    write_pid(process.pid)
    info(f"FastSocket server started with PID {process.pid}")

    # Optionally, you can wait for a short period to ensure the server starts correctly
    time.sleep(2)

    # Check if the server is still running
    if process.poll() is None:
        success(f"FastSocket server is running on {host}:{port}")
    else:
        stdout, stderr = process.communicate()
        error(f"FastSocket server failed to start.\nSTDOUT: {stdout}\nSTDERR: {stderr}")
        remove_pid()
        raise typer.Exit(code=1)


@app.command()
def stop():
    """
    Stop the FastSocket server gracefully.
    """
    if not is_server_running():
        error("FastSocket server is not running.")
        raise typer.Exit(code=1)

    pid = get_server_pid()
    if pid is None:
        error("Invalid PID file. Cannot stop the server.")
        raise typer.Exit(code=1)

    info(f"Stopping FastSocket server with PID {pid}")
    try:
        os.kill(pid, signal.SIGTERM)
        # Wait for the process to terminate
        for _ in range(10):
            if not is_server_running():
                break
            time.sleep(0.5)
        else:
            warning("Server did not terminate gracefully. Killing the process.")
            os.kill(pid, signal.SIGKILL)

        remove_pid()
        success("FastSocket server has been stopped successfully.")
    except OSError as e:
        error(f"Error stopping the server: {e}")
        raise typer.Exit(code=1)


@app.command()
def status():
    """
    Show the current status of the FastSocket server.
    """
    if is_server_running():
        pid = get_server_pid()
        info(f"FastSocket server is running with PID {pid}")
        # Optionally, you can check the host and port by connecting to the server or reading a config
    else:
        info("FastSocket server is not running.")


@app.command()
def list_events(directory: str = EVENTS_DEFAULT_DIR):
    """
    List all registered event names and their corresponding handler functions.
    """
    info(f"Listing events from directory '{directory}'")
    events: List[str] = []
    handlers: List[str] = []

    try:
        for filename in os.listdir(directory):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = filename[:-3]
                module_path = f"fastsocket.events.{module_name}"
                module = importlib.import_module(module_path)
                if hasattr(module, 'handle_event'):
                    handle_event = getattr(module, 'handle_event')
                    if callable(handle_event):
                        event_name = ''.join([word.capitalize() for word in module_name.split('_')])
                        events.append(event_name)
                        handlers.append(f"{module_name}.handle_event")
        if events:
            info("Registered Events:")
            for event, handler in zip(events, handlers):
                info(f"  - {event}: {handler}")
        else:
            info("No events registered.")
    except Exception as e:
        error(f"Failed to list events: {e}")
        raise typer.Exit(code=1)


@app.command("reload")
def reload_events():
    """Trigger the FastSocket server to reload event handlers."""
    reload_url = "http://localhost:8000/admin/reload-events"
    try:
        response = httpx.post(reload_url)
        if response.status_code == 200:
            info("Event handlers reloaded successfully.")
            print("Event handlers reloaded successfully.")
        else:
            error(f"Failed to reload event handlers. Status: {response.status_code}")
            print(f"Failed to reload event handlers. Status: {response.status_code}")
    except Exception as e:
        error(f"Error reloading event handlers: {e}")
        print(f"Error reloading event handlers: {e}")


if __name__ == "__main__":
    app()
