# src/fastsocket/api.py
from contextlib import asynccontextmanager

import socketio
from fastapi import FastAPI, HTTPException
from loguru import logger
import sys

from fastsocket.event_registry import register_events
from fastsocket.logger import info, error

# Define a dictionary to store state
state = {"event_registry_initialized": False}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Startup Logic ---
    info("Starting up FastSocket application...")

    try:
        # Register event handlers on startup
        await register_events(event_directory="src/fastsocket/events", reload=False)
        state["event_registry_initialized"] = True
        info("Event handlers registered successfully.")
        yield  # Application starts receiving requests after this point
    finally:
        # --- Shutdown Logic ---
        info("Shutting down FastSocket application...")
        # Example cleanup task: Set state to false or disconnect clients
        state["event_registry_initialized"] = False
        info("Resources cleaned up. FastSocket has shut down.")


# Initialize FastAPI application
app = FastAPI(
    title="FastSocket API",
    description="A message queue abstraction layer with Socket.IO and FastAPI.",
    version="1.0.0",
    lifespan=lifespan
)

# Initialize Socket.IO server
sio = socketio.AsyncServer(
    async_mode='asgi',
    logger=True,
    engineio_logger=True,
    cors_allowed_origins=[
        'http://localhost:3000',
        'https://admin.socket.io',
    ]
)

# Create ASGI app for Socket.IO and wrap FastAPI app
socket_app = socketio.ASGIApp(sio, other_asgi_app=app)


@app.get("/")
async def read_root():
    return {"message": "FastSocket API is running."}


@app.on_event("shutdown")
async def shutdown_event():
    info("Shutting down FastSocket server...")
    # Perform any necessary cleanup here
    await sio.disconnect()
    info("Shutdown complete.")


# Create the reload endpoint
@app.post("/admin/reload-events")
async def reload_events():
    """Endpoint to reload event handlers."""
    try:
        await register_events(event_directory="src/fastsocket/events", reload=True)
        info("Event handlers reloaded successfully.")
        return {"status": "success", "message": "Event handlers reloaded successfully."}
    except Exception as e:
        error(f"Failed to reload event handlers: {e}")
        raise HTTPException(status_code=500, detail="Failed to reload event handlers.")
