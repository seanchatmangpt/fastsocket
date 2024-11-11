# FastSocket

**FastSocket** is an advanced, high-performance, event-driven real-time messaging and logging system architected with a
robust integration of **FastAPI**, **Socket.IO**, **AsyncAPI**, **Pydantic**, **Typer**, **Logfire**, and **ReactiveX (
RxPY)**. Designed to facilitate scalable, maintainable, and efficient real-time applications, FastSocket is ideal for
complex systems requiring seamless event handling, data validation, and reactive programming paradigms.

![FastSocket Architecture](https://your-portfolio.com/fastsocket-architecture.png)

---

## 📄 Abstract

In the realm of real-time web applications, efficient event handling and robust data validation are paramount.
FastSocket leverages the synergistic capabilities of FastAPI for asynchronous web serving, Socket.IO for real-time
bidirectional communication, AsyncAPI for standardized event-driven architecture definitions, Pydantic for stringent
data validation, Typer for intuitive CLI interactions, Logfire for comprehensive logging and monitoring, and ReactiveX (
RxPY) for reactive programming paradigms. This README delineates the intricate architecture, underlying technologies,
implementation strategies, and operational workflows that collectively empower FastSocket to deliver unparalleled
performance and scalability in real-time applications.

---

## 🔍 Introduction

FastSocket emerges as a cutting-edge solution for developers seeking to build real-time, event-driven applications with
minimal overhead and maximal scalability. By harnessing the power of modern Python frameworks and libraries, FastSocket
streamlines the development process, ensuring consistency, reliability, and maintainability across both backend and
frontend components.

### Key Objectives

- **Real-Time Communication**: Facilitate instant, bidirectional communication between clients and servers.
- **Standardized Event Definitions**: Utilize AsyncAPI to define and manage event-driven architectures.
- **Robust Data Validation**: Implement Pydantic models to ensure data integrity and type safety.
- **Intuitive CLI Management**: Employ Typer to create a user-friendly command-line interface for server and event
  management.
- **Comprehensive Logging**: Integrate Logfire for real-time log monitoring and analysis.
- **Reactive Programming**: Leverage RxPY to handle complex event streams and reactive data flows.

---

## 🏗️ Architecture

FastSocket's architecture is meticulously designed to promote scalability, maintainability, and efficiency. The system
is compartmentalized into distinct modules, each responsible for specific functionalities, ensuring a clean separation
of concerns.

### Architectural Components

1. **FastAPI Backend**:
    - Serves as the asynchronous web server handling API requests.
    - Integrates with Socket.IO for real-time event handling.
    - Utilizes AsyncAPI for defining event-driven interactions.

2. **Socket.IO Integration**:
    - Facilitates real-time, bidirectional communication between clients and the server.
    - Manages WebSocket connections, event broadcasting, and room management.

3. **AsyncAPI Specification**:
    - Serves as the single source of truth for defining event channels, messages, and payloads.
    - Drives the automatic generation of event handlers and frontend components.

4. **Pydantic Models**:
    - Ensures rigorous data validation and type enforcement for incoming and outgoing data.
    - Enhances data integrity across the application.

5. **Typer CLI**:
    - Provides a command-line interface for managing server operations, event registrations, and log viewing.
    - Streamlines administrative tasks and operational workflows.

6. **Logfire Integration**:
    - Offers real-time log monitoring and visualization.
    - Enhances observability and debugging capabilities.

7. **ReactiveX (RxPY)**:
    - Implements reactive programming paradigms to handle complex event streams.
    - Enables responsive and scalable event processing.

### Architectural Diagram

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|   Frontend     | <---> |   Socket.IO    | <---> |    FastAPI     |
|   (Nuxt.js)    |       |    Server      |       |    Backend     |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
        |                        |                        |
        |                        |                        |
        v                        v                        v
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  ReactiveX     |       |   Logfire      |       |  AsyncAPI      |
|   (RxPY)       |       |   Logging      |       |  Specification |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
```

---

## 🛠️ Technologies Used

### Backend

- **FastAPI**: An asynchronous, high-performance web framework for building APIs with Python 3.6+ based on standard
  Python type hints.
- **Socket.IO**: A library for real-time, bidirectional, and event-based communication between the browser and the
  server.
- **AsyncAPI**: A specification for defining event-driven architectures, providing a standardized way to document and
  visualize APIs.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Typer**: A library for building command-line interface (CLI) applications with ease.
- **Logfire**: A logging platform that provides real-time log monitoring and analysis.
- **ReactiveX (RxPY)**: A library for composing asynchronous and event-based programs using observable sequences.

### Frontend

- **Nuxt.js**: A progressive framework based on Vue.js for building server-side rendered (SSR) applications and static
  websites.
- **Vue.js**: A progressive JavaScript framework for building user interfaces.

### Other Tools

- **Poetry**: A tool for dependency management and packaging in Python.
- **Docker & Docker Compose**: Tools for containerizing applications and orchestrating multi-container Docker
  applications.
- **Pytest**: A robust testing framework for Python.

---

## 📂 Project Structure

```plaintext
fastsocket/
├── Dockerfile                     # Docker configuration for containerizing the application
├── README.md                      # Comprehensive project documentation
├── docker-compose.yml             # Docker Compose configuration for multi-service orchestration
├── fastsocket.pid                 # PID file to track the running server process
├── logs/
│   └── debug.log                  # Log file generated by Loguru for structured logging
├── poetry.lock                    # Locked dependencies for Poetry
├── pyproject.toml                 # Poetry project configuration
├── src/
│   └── fastsocket/
│       ├── __init__.py
│       ├── api.py                 # FastAPI application setup with event and lifespan handling
│       ├── cli.py                 # Typer CLI for server and log management
│       ├── commands/
│       │   ├── __init__.py
│       │   └── log_cmds.py         # CLI commands for log management
│       ├── event_registry.py      # Module for registering and reloading event handlers
│       ├── events/                # Directory containing event handler modules
│       │   ├── __init__.py
│       │   ├── example_event.py
│       │   ├── on_light_measured.py
│       │   ├── send_notification.py
│       │   ├── user_deleted.py
│       │   ├── user_signed_up.py
│       │   └── user_updated.py
│       ├── happy_client.py        # Example client implementation for testing
│       ├── logger.py              # Configures Loguru for structured logging
│       └── logs/
│           └── debug.log
└── tests/
    ├── __init__.py
    ├── test_api.py                 # Tests for FastAPI endpoints
    ├── test_cli.py                 # Tests for CLI commands
    └── test_import.py              # Tests for module imports and integrity
```

### Detailed Breakdown

- **Dockerfile & docker-compose.yml**: Facilitate containerization and orchestration, enabling seamless deployment
  across various environments.
- **fastsocket.pid**: Maintains the Process ID of the running server, aiding in server management operations like stop
  and status checks.
- **logs/debug.log**: Centralized log file capturing structured logs from the application, enhancing observability and
  debugging.
- **pyproject.toml & poetry.lock**: Manage project dependencies and configurations using Poetry, ensuring reproducible
  builds.
- **src/fastsocket/**: Core application logic encompassing API setup, CLI commands, event handling, logging
  configuration, and example client implementations.
    - **api.py**: Configures the FastAPI application, integrates Socket.IO, manages lifespan events, and defines API
      endpoints.
    - **cli.py**: Implements the Typer-powered CLI, offering commands for starting, stopping, reloading the server, and
      managing logs.
    - **commands/log_cmds.py**: Houses specific CLI commands related to log viewing, tailing, and clearing.
    - **event_registry.py**: Handles dynamic registration and reloading of event handlers based on AsyncAPI
      specifications.
    - **events/**: Contains individual event handler modules, each corresponding to a specific event type defined in
      AsyncAPI.
    - **happy_client.py**: Serves as an example client for testing and demonstrating real-time event interactions.
    - **logger.py**: Sets up Loguru with configurations for log rotation, formatting, and log level management.
- **tests/**: Encompasses a suite of tests ensuring the reliability and correctness of API endpoints, CLI
  functionalities, and module imports.

---

## 🔧 Installation

### Prerequisites

- **Python** 3.13+
- **Poetry** for dependency management
- **Docker** & **Docker Compose** (optional, for containerization)
- **Node.js** & **npm** (if integrating with the Nuxt.js frontend)

### Clone the Repository

```bash
git clone https://github.com/your-username/fastsocket.git
cd fastsocket
```

### Install Backend Dependencies

Using Poetry:

```bash
poetry install
```

Activate the virtual environment:

```bash
poetry shell
```

### Configure Environment Variables

Create a `.env` file in the project root with the following variables:

```dotenv
API_KEY=<your_api_key>
LOG_LEVEL=DEBUG
HOST=0.0.0.0
PORT=8000
EVENTS_DIR=src/fastsocket/events
LOG_DIR=logs
```

Ensure that sensitive information like `API_KEY` is securely managed and not exposed publicly.

---

## 🛠️ Usage

FastSocket offers a comprehensive Command-Line Interface (CLI) powered by **Typer**, enabling efficient management of
server operations, event handling, and log monitoring.

### Initialize CLI

Ensure that the virtual environment is activated:

```bash
poetry shell
```

### Available CLI Commands

Invoke the CLI using the `fs7` command:

```bash
fs7 --help
```

#### Output

```
Logfire project URL: https://logfire.pydantic.dev/seanchatmangpt/fastsocket
Server initialized for asgi.

 Usage: fs7 [OPTIONS] COMMAND [ARGS]...

╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                           │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                    │
│ --help                        Show this message and exit.                                                                                         │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ asyncapi                  Manage AsyncAPI files and generate documentation.                                                                       │
│ list-events               List all registered event names and their corresponding handler functions.                                              │
│ log                       Manage log files and view logs.                                                                                         │
│ register-events-command   Register event handlers from a specified directory.                                                                     │
│ reload                    Trigger the FastSocket server to reload event handlers.                                                                 │
│ start                     Start the FastSocket server.                                                                                            │
│ status                    Show the current status of the FastSocket server.                                                                       │
│ stop                      Stop the FastSocket server gracefully.                                                                                  │
╰───────────────────────────────────────────────────────────────────────
```

### Detailed Command Descriptions

#### 1. Start the Server

```bash
fs7 start
```

- **Description**: Initializes and starts the FastAPI server with Socket.IO support. It also writes the server PID
  to `fastsocket.pid` for process management.
- **Behavior**:
    - Checks if the server is already running.
    - Starts the server using Uvicorn.
    - Writes the server PID for tracking.
    - Provides feedback on server status.

#### 2. Stop the Server

```bash
fs7 stop
```

- **Description**: Sends a termination signal to the running FastSocket server process, ensuring a graceful shutdown and
  resource cleanup.
- **Behavior**:
    - Reads the PID from `fastsocket.pid`.
    - Sends a SIGTERM signal to the process.
    - Waits for the process to terminate gracefully.
    - Removes the PID file upon successful shutdown.

#### 3. Check Server Status

```bash
fs7 status
```

- **Description**: Reports the current status of the FastSocket server, including the process ID if running.
- **Behavior**:
    - Checks for the existence of `fastsocket.pid`.
    - Verifies if the process is active.
    - Outputs the server status accordingly.

#### 4. Register Event Handlers

```bash
fs7 register-events-command --directory src/fastsocket/events
```

- **Description**: Scans the provided directory for event handler modules and registers them with the server.
- **Behavior**:
    - Loads and registers all event handlers defined in the specified directory.
    - Validates handler integrity and dependencies.
    - Logs registration status and any encountered issues.

#### 5. Reload Event Handlers

```bash
fs7 reload
```

- **Description**: Reloads the event handlers dynamically, allowing updates to event processing logic without server
  downtime.
- **Behavior**:
    - Sends a POST request to the `/admin/reload-events` endpoint.
    - Triggers the server to re-import and register event handlers.
    - Provides feedback on the success or failure of the reload operation.

#### 6. Manage Logs

##### View Logs

```bash
fs7 log view-logs --lines 100
```

- **Description**: Displays the last 100 lines from `logs/debug.log`, providing insights into server operations and
  event handling.
- **Options**:
    - `--lines`: Number of log lines to display (default: 100).

##### Clear Logs

```bash
fs7 log clear-logs
```

- **Description**: Empties the `logs/debug.log` file, useful for resetting log data.
- **Behavior**:
    - Truncates the log file.
    - Confirms the action upon completion.

##### Tail Logs

```bash
fs7 log tail-logs
```

- **Description**: Streams new log entries as they are written, similar to the `tail -f` command. Press `Ctrl+C` to stop
  tailing.
- **Behavior**:
    - Continuously reads the log file.
    - Outputs new log entries in real-time.

#### 7. Manage AsyncAPI

```bash
fs7 asyncapi --help
```

- **Description**: Commands related to managing AsyncAPI files and generating corresponding documentation.
- **Subcommands**:
    - `export`: Generate documentation from AsyncAPI specifications.
    - `validate`: Validate AsyncAPI YAML files against the specification.

#### 8. List Events

```bash
fs7 list-events
```

- **Description**: Displays a list of all events currently registered in the FastSocket server along with their
  corresponding handler functions.
- **Behavior**:
    - Enumerates registered events.
    - Outputs event names and associated handlers.

---

## 🔄 API Reference

FastSocket exposes several API endpoints for managing events and monitoring server status. Below is a detailed reference
for each endpoint, including request parameters, responses, and usage examples.

### 1. Get All Events

```http
GET /api/events
```

- **Description**: Retrieves a list of all registered events along with their handler functions.
- **Parameters**:
    - `api_key` (string, required): API access key for authentication.
- **Response**:

```json
[
  {
    "event_id": "1",
    "name": "user_signed_up",
    "handler": "user_signed_up.handle_event"
  },
  {
    "event_id": "2",
    "name": "user_deleted",
    "handler": "user_deleted.handle_event"
  }
  // ... other events
]
```

### 2. Get Specific Event

```http
GET /api/events/{event_id}
```

- **Description**: Retrieves details of a specific event by its unique ID.
- **Parameters**:
    - `event_id` (string, required): Unique identifier of the event.
- **Response**:

```json
{
  "event_id": "1",
  "name": "user_signed_up",
  "handler": "user_signed_up.handle_event"
}
```

### 3. Trigger an Event

```http
POST /api/events
```

- **Description**: Triggers a specific event with the provided payload.
- **Parameters**:
    - `name` (string, required): Name of the event to trigger.
    - `payload` (json, optional): Data associated with the event.
- **Request Body**:

```json
{
  "name": "user_signed_up",
  "payload": {
    "user_id": "12345",
    "email": "user@example.com"
  }
}
```

- **Response**:

```json
{
  "status": "success",
  "message": "user_signed_up handled successfully."
}
```

### 4. Admin Reload Events

```http
POST /admin/reload-events
```

- **Description**: Reloads all event handlers without restarting the server.
- **Security Note**: This endpoint should be secured (e.g., via authentication) to prevent unauthorized access.
- **Response**:

```json
{
  "status": "success",
  "message": "Event handlers reloaded successfully."
}
```

---

## 🗂️ Logging

FastSocket employs **Loguru** for structured and efficient logging, ensuring comprehensive tracking of server
operations, event handling, and CLI activities.

### Log Configuration

- **Log File Path**: `logs/debug.log`
- **Rotation Policy**: Logs are rotated when they reach 1 MB in size.
- **Retention Policy**: Logs are retained for 10 days, after which they are automatically deleted.
- **Log Levels**: Supports standard log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).

### Log Management Commands

FastSocket's CLI provides commands to manage and view logs efficiently.

#### 1. View Logs

```bash
fs7 log view-logs --lines 100
```

- **Description**: Displays the last 100 lines of the log file.
- **Options**:
    - `--lines` (int): Number of log lines to display (default: 100).

#### 2. Clear Logs

```bash
fs7 log clear-logs
```

- **Description**: Clears all contents of the log file, effectively resetting it.

#### 3. Tail Logs

```bash
fs7 log tail-logs
```

- **Description**: Streams new log entries in real-time, similar to the Unix `tail -f` command.
- **Usage**: Press `Ctrl+C` to stop tailing.

### Logfire Integration

FastSocket integrates with **Logfire** to provide advanced log management and visualization capabilities.

- **Logfire Project URL
  **: [https://logfire.pydantic.dev/seanchatmangpt/fastsocket](https://logfire.pydantic.dev/seanchatmangpt/fastsocket)
- **Features**:
    - Real-time log streaming.
    - Search and filter logs based on severity and keywords.
    - Visual dashboards for monitoring log trends and anomalies.

---

## 🔌 Integration with AsyncAPI

**AsyncAPI** serves as the cornerstone for defining the event-driven architecture of FastSocket. It provides a
standardized specification for asynchronous APIs, facilitating seamless integration between backend event handlers and
frontend components.

### Benefits of Using AsyncAPI

- **Standardization**: Ensures consistent event definitions across the system.
- **Automated Code Generation**: Enables the automatic generation of event handlers and frontend components based on the
  specification.
- **Documentation**: Generates comprehensive documentation, enhancing maintainability and developer onboarding.
- **Validation**: Ensures that event payloads conform to predefined schemas, reducing runtime errors.

### AsyncAPI Workflow in FastSocket

1. **Define Events**: Specify event channels, messages, and payloads in the `asyncapi.yaml` file.
2. **Generate Handlers and Components**: Utilize the CLI commands to generate Python event handlers and Vue.js frontend
   components based on the AsyncAPI specification.
3. **Register Handlers**: Automatically register generated handlers with the FastAPI and Socket.IO server.
4. **Synchronize Frontend**: Frontend components interact with the backend via Socket.IO, adhering to the event
   definitions in AsyncAPI.

### Example AsyncAPI Specification

```yaml
asyncapi: '2.6.0'
info:
  title: FastSocket API
  version: '1.0.0'
channels:
  user_signed_up:
    publish:
      summary: User Signed Up Event
      message:
        contentType: application/json
        payload:
          type: object
          properties:
            user_id:
              type: string
            email:
              type: string
  user_deleted:
    publish:
      summary: User Deleted Event
      message:
        contentType: application/json
        payload:
          type: object
          properties:
            user_id:
              type: string
```

---

## 🧬 Implementation Details

### 1. Event Registration and Handling

FastSocket dynamically registers event handlers based on the AsyncAPI specification, ensuring that each event has a
corresponding backend handler and frontend component.

#### Event Registry (`event_registry.py`)

- **Functionality**:
    - Parses AsyncAPI definitions.
    - Dynamically imports and registers event handler modules.
    - Supports hot-reloading of event handlers to facilitate real-time updates without server restarts.
- **Key Components**:
    - **Dynamic Importing**: Uses `importlib` to load event handler modules at runtime.
    - **Pydantic Integration**: Utilizes Pydantic models for strict data validation of incoming event payloads.
    - **Socket.IO Integration**: Registers asynchronous event handlers with the Socket.IO server for real-time
      communication.

#### Example Event Handler (`user_signed_up.py`)

```python
from pydantic import BaseModel
from loguru import logger


class UserSignedUpPayload(BaseModel):
    user_id: str
    email: str


async def handle_event(sid: str, data: UserSignedUpPayload, sio):
    logger.info(f"Handling user_signed_up for SID '{sid}' with data: {data.model_dump()}")
    # Business logic: e.g., store user in database
    await sio.emit("user_signed_up_ack", {"status": "success", "message": "User signed up successfully"}, room=sid)
```

### 2. Command-Line Interface (CLI)

The CLI, built with **Typer**, offers an intuitive interface for managing server operations, event handlers, and logs.

#### CLI Structure (`cli.py`)

- **Commands**:
    - `start`: Launches the FastSocket server.
    - `stop`: Gracefully shuts down the server.
    - `status`: Checks if the server is running.
    - `register-events-command`: Registers event handlers from a specified directory.
    - `reload`: Triggers the server to reload event handlers without restarting.
    - `log`: Subcommands for managing logs (`view-logs`, `clear-logs`, `tail-logs`).
    - `asyncapi`: Manage AsyncAPI files and generate documentation.
    - `list-events`: Lists all registered events and their handlers.

#### Example CLI Command (`start`)

```python
@app.command()
def start(host: str = DEFAULT_HOST, port: int = DEFAULT_PORT):
    """
    Start the FastSocket server.
    """
    if is_server_running():
        logger.error("FastSocket server is already running.")
        raise typer.Exit(code=1)

    logger.info(f"Starting FastSocket server on {host}:{port}")

    # Start the server as a subprocess using Uvicorn
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "fastsocket.api:app", "--host", host, "--port", str(port)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Write the PID to the PID file
    write_pid(process.pid)
    logger.info(f"FastSocket server started with PID {process.pid}")

    # Optionally, wait and check if the server is running
    time.sleep(2)
    if process.poll() is None:
        logger.success(f"FastSocket server is running on {host}:{port}")
    else:
        stdout, stderr = process.communicate()
        logger.error(f"FastSocket server failed to start.\nSTDOUT: {stdout}\nSTDERR: {stderr}")
        remove_pid()
        raise typer.Exit(code=1)
```

### 3. Logging with Logfire

FastSocket employs **Loguru** for structured logging, capturing detailed information about server operations, event
handling, and CLI activities.

#### Logger Configuration (`logger.py`)

```python
from loguru import logger
import sys

# Remove the default logger to prevent duplicate logs
logger.remove()

# Configure Loguru to log to stdout and a file with rotation and retention
logger.add(sys.stdout, format="{time} {level} {message}", level="INFO")
logger.add("logs/debug.log", rotation="1 MB", level="DEBUG", retention="10 days")
```

#### Logfire Integration

- **Logfire Project URL
  **: [https://logfire.pydantic.dev/seanchatmangpt/fastsocket](https://logfire.pydantic.dev/seanchatmangpt/fastsocket)
- **Functionality**:
    - Real-time log streaming and visualization.
    - Search, filter, and analyze logs based on severity and keywords.
    - Integration with the CLI for seamless log management.

### 4. Reactive Programming with RxPY

FastSocket utilizes **ReactiveX (RxPY)** to handle complex event streams and reactive data flows, enabling responsive
and scalable event processing.

#### Event Stream Management

- **RxPY Subjects**: Acts as bridges for event streams, allowing for multicasting and reactive transformations.
- **Subscriptions**: Frontend components can subscribe to event observables, enabling real-time data updates and
  interactions.

#### Example Reactive Flow

```python
import reactivex as rx
from loguru import logger

# Subject to act as a bridge for event streams
event_subjects = {}


def create_event_stream(event_name: str):
    if event_name not in event_subjects:
        event_subjects[event_name] = rx.Subject()
    return event_subjects[event_name]


# Example: Emitting an event
def emit_event(event_name: str, data: dict):
    logger.debug(f"Emitting event '{event_name}' with data: {data}")
    stream = create_event_stream(event_name)
    stream.on_next(data)


# Example: Subscribing to an event
def subscribe_to_event(event_name: str, callback):
    stream = create_event_stream(event_name)
    subscription = stream.subscribe(
        on_next=lambda data: callback(data),
        on_error=lambda e: logger.error(f"Error in event '{event_name}': {e}")
    )
    return subscription
```

---

## 📚 Code Generation with AsyncAPI

FastSocket automates the generation of backend event handlers and frontend Vue components based on **AsyncAPI**
specifications, ensuring consistency and reducing manual coding efforts.

### Templates

#### 1. Python Handler Template

Defines a Pydantic model for data validation and an asynchronous event handler function.

```python
from pydantic import BaseModel
from loguru import logger


# Define Pydantic model for validation
class {{operation_name | camelize}}Payload(BaseModel):


    { %
for field, type in fields.items() %}
{{field}}: {{type}}
{ % endfor %}

# Event handler function
async def handle_event(sid: str, data: {{operation_name | camelize}}Payload, sio

):
logger.info(f"Handling {{ operation_name }} for SID '{sid}' with data: {data.model_dump()}")
# Add your logic here, such as updating database records, etc.
await sio.emit("{{ operation_name }}_ack",
               {"status": "success",
                "message": "{{ operation_name }} handled successfully"},
               room=sid)
```

#### 2. Vue Component Template

Creates a Vue component with a button to trigger events and displays received data.

```html

<template>
    <div>
        <button @click="handle{{ operation_name | camelize }}">Send {{ operation_name | camelize }}</button>
        <div v-if="receivedData">Callback Data: {{ receivedData }}</div>
        <div v-if="observedData">Observable Data: {{ observedData }}</div>
    </div>
</template>

<script setup>
    import {ref, onUnmounted} from 'vue';
    import {useOperation} from '@/composables/useOperation';

    const {send
    {
        {
            operation_name | camelize
        }
    }
    ,
    receive
    {
        {
            operation_name | camelize
        }
    }
    ,
    observe
    {
        {
            operation_name | camelize
        }
    }
    }
    = useOperation('{{ operation_name }}');

    const receivedData = ref(null);
    const observedData = ref(null);

    // Callback-based receive example
    const unsubscribeCallback = receive
    {
        {
            operation_name | camelize
        }
    }
    ((data) => {
        receivedData.value = data;
        console.log('Received data (callback):', data);
    });

    // Observable-based receive example
    const {observable, unsubscribe: unsubscribeObservable} = observe
    {
        {
            operation_name | camelize
        }
    }
    ();
    const subscription = observable.subscribe((data) => {
        observedData.value = data;
        console.log('Received data (observable):', data);
    });

    // Send data to server
    const handle
    {
        {
            operation_name | camelize
        }
    }
    = async () => {
        try {
            const response = await send
            {
                {
                    operation_name | camelize
                }
            }
            ({
            {%
                for field in fields %
            }
            {
                {
                    field
                }
            }
        :
            '{{ field | default }}'
            {
                {
                    ','
                    if not loop.last
                }
            }
            {%
                endfor %
            }
        })
            ;
            console.log('Server acknowledgment:', response);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    // Cleanup on component unmount
    onUnmounted(() => {
        unsubscribeCallback();
        unsubscribeObservable();
        subscription.unsubscribe();
    });
</script>
```

### CLI Commands for Code Generation

#### Generate Backend Handlers

```bash
fs7 handlers --asyncapi-file path/to/asyncapi.yaml --output-dir src/fastsocket/events
```

- **Description**: Parses the specified AsyncAPI YAML file and generates corresponding Python event handler files in the
  designated directory.
- **Behavior**:
    - Reads the AsyncAPI specification.
    - Extracts event definitions and payload schemas.
    - Renders Python handler templates with Pydantic models.
    - Saves the generated handlers to the output directory.

#### Generate Vue Pages

```bash
fs7 pages --asyncapi-file path/to/asyncapi.yaml --output-dir path/to/nuxt/pages
```

- **Description**: Parses the specified AsyncAPI YAML file and generates corresponding Vue.js component files in the
  designated directory.
- **Behavior**:
    - Reads the AsyncAPI specification.
    - Extracts event definitions and payload schemas.
    - Renders Vue component templates.
    - Saves the generated components to the output directory.

---

## 🐳 Deployment

FastSocket is designed for seamless deployment using containerization technologies like **Docker** and orchestration
tools like **Docker Compose**. This ensures consistent environments across development, testing, and production,
facilitating scalability and maintainability.

### Docker Deployment

#### Dockerfile

The Dockerfile defines the container image for FastSocket, ensuring all dependencies are included and the application
runs consistently.

```dockerfile
# Use official Python image as base
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential

# Install Poetry
RUN pip install --upgrade pip
RUN pip install poetry

# Copy project files
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . /app/

# Expose port
EXPOSE 8000

# Start the application
CMD ["uvicorn", "src.fastsocket.api:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Docker Compose

Docker Compose orchestrates multiple services, such as the FastSocket server and any additional dependencies like
databases or log management services.

```yaml
version: '3.8'

services:
  fastsocket:
    build: .
    container_name: fastsocket
    ports:
      - "8000:8000"
    volumes:
      - .:/app
      - ./logs:/app/logs
    environment:
      - API_KEY=${API_KEY}
      - LOG_LEVEL=${LOG_LEVEL}
      - HOST=0.0.0.0
      - PORT=8000
    restart: unless-stopped

  # Example: Logfire service (if required)
  logfire:
    image: logfire/logfire:latest
    container_name: logfire
    ports:
      - "9000:9000"
    volumes:
      - ./logs:/var/log/fastsocket
    environment:
      - LOG_DIR=/var/log/fastsocket
    restart: unless-stopped
```

### Steps to Deploy with Docker Compose

1. **Build and Run Containers**:

    ```bash
    docker-compose up --build
    ```

2. **Access Services**:

    - **FastAPI Server**: `http://localhost:8000`
    - **Logfire Viewer**: `http://localhost:9000` (if integrated)

3. **Environment Variables**:

   Ensure that a `.env` file exists with the necessary environment variables:

    ```dotenv
    API_KEY=<your_api_key>
    LOG_LEVEL=DEBUG
    ```

4. **Scaling Services**:

   Docker Compose allows scaling services as needed:

    ```bash
    docker-compose up --scale fastsocket=3 --build
    ```

   This command scales the FastSocket service to three instances, enhancing performance and reliability.

---

## 🧪 Testing

FastSocket incorporates a comprehensive test suite to ensure reliability, correctness, and robustness. Utilizing *
*Pytest**, the tests cover API endpoints, CLI commands, and module integrity.

### Running Tests

Activate the virtual environment and execute the test suite:

```bash
poetry shell
pytest tests/
```

### Test Coverage

- **API Endpoints (`test_api.py`)**:
    - Validates the correctness of API responses.
    - Ensures proper handling of event triggers and data validation.
    - Tests error responses and edge cases.

- **CLI Commands (`test_cli.py`)**:
    - Tests the functionality of each CLI command.
    - Verifies server start, stop, reload operations.
    - Ensures log management commands work as intended.

- **Module Imports (`test_import.py`)**:
    - Ensures all modules and event handlers can be imported without errors.
    - Validates the integrity of dynamically generated code.

### Example Test Case (`test_api.py`)

```python
import pytest
from fastapi.testclient import TestClient
from src.fastsocket.api import app

client = TestClient(app)


def test_get_events():
    response = client.get("/api/events", headers={"api_key": "test_key"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_trigger_event():
    event_payload = {
        "name": "user_signed_up",
        "payload": {
            "user_id": "12345",
            "email": "user@example.com"
        }
    }
    response = client.post("/api/events", json=event_payload, headers={"api_key": "test_key"})
    assert response.status_code == 200
    assert response.json()["status"] == "success"
```

---

## ⚙️ Optimizations

FastSocket integrates several optimizations to enhance performance, scalability, and developer experience.

### 1. Asynchronous Operations

Utilizes FastAPI's asynchronous capabilities and Socket.IO's async support to handle multiple concurrent connections
efficiently, ensuring non-blocking operations and high throughput.

### 2. Hot-Reloading of Event Handlers

Implements a mechanism to reload event handlers dynamically without necessitating a server restart. This is achieved
through the `/admin/reload-events` endpoint and the `reload` CLI command, allowing for rapid development and deployment
cycles.

### 3. Structured and Rotated Logging

Employs Loguru's advanced logging features, including log rotation and retention policies, to manage log files
effectively, preventing disk space exhaustion and ensuring log data is organized and accessible.

### 4. Reactive Programming Paradigm

Incorporates ReactiveX (RxPY) to manage complex event streams and reactive data flows, enabling responsive and scalable
event processing.

### 5. Containerization with Docker

Facilitates consistent and reproducible deployment environments through Docker and Docker Compose, enhancing scalability
and simplifying infrastructure management.

### 6. Modular Codebase

Adopts a modular project structure, promoting maintainability and scalability. Event handlers are organized into
separate modules, and the CLI commands are compartmentalized, ensuring clean code organization.

---

## 🛣️ Roadmap

FastSocket is an evolving project with plans to incorporate additional features and improvements to enhance its
capabilities and usability.

### Planned Enhancements

1. **Frontend Dashboard**:
    - Develop a Nuxt.js-based dashboard for monitoring events, managing handlers, and visualizing real-time data
      streams.
    - Integrate with Logfire for advanced log analytics within the dashboard.

2. **Authentication and Authorization**:
    - Implement JWT-based authentication for securing API endpoints and Socket.IO connections.
    - Introduce role-based access controls to manage user permissions.

3. **Advanced Log Filtering and Search**:
    - Enhance log viewing capabilities with dynamic filtering by severity levels, keywords, and timestamps.
    - Implement full-text search within logs for efficient troubleshooting.

4. **Multi-Tenancy Support**:
    - Allow multiple isolated environments within the same FastSocket instance, catering to different client groups or
      application segments.

5. **Enhanced Event Handling**:
    - Support for more complex event processing, such as event chaining, transformations, and conditional handling.
    - Integrate with external services for enriched event workflows.

6. **Performance Monitoring and Metrics**:
    - Incorporate monitoring tools to track server performance, event processing times, and system health.
    - Provide real-time metrics dashboards for operational insights.

7. **Automated Documentation Generation**:
    - Leverage AsyncAPI to automatically generate comprehensive documentation for both backend and frontend components.
    - Integrate with documentation platforms like Swagger UI for enhanced accessibility.

---

## 👥 Contributing

Contributions are highly encouraged to help improve FastSocket. Whether it's reporting bugs, suggesting features, or
contributing code, your involvement is invaluable.

### Steps to Contribute

1. **Fork the Repository**

   Click the "Fork" button at the top-right corner of the repository page to create your own fork.

2. **Clone Your Fork**

    ```bash
    git clone https://github.com/your-username/fastsocket.git
    cd fastsocket
    ```

3. **Create a Feature Branch**

    ```bash
    git checkout -b feature/your-feature-name
    ```

4. **Commit Your Changes**

    ```bash
    git commit -m "Add your descriptive commit message"
    ```

5. **Push to Your Fork**

    ```bash
    git push origin feature/your-feature-name
    ```

6. **Open a Pull Request**

   Navigate to the original repository and click on "Compare & pull request" to submit your changes for review.

### Code of Conduct

Please adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and respectful environment for all
contributors.

### Reporting Issues

If you encounter any issues or have feature requests, please open an issue in
the [Issue Tracker](https://github.com/your-username/fastsocket/issues).

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 📞 Contact

**Sean Chatman** (He/Him)  
Full Stack Developer specializing in **Front End Generative AI Web Development** with expertise in **TypeScript**, *
*React**, **Vue**, and **Python**.

- **Portfolio**: [https://seanchatmangpt.com](https://seanchatmangpt.com)
- **Email**: [sean@example.com](mailto:sean@example.com)
- **LinkedIn**: [linkedin.com/in/seanchatmangpt](https://linkedin.com/in/seanchatmangpt)
- **GitHub**: [github.com/seanchatmangpt](https://github.com/seanchatmangpt)

---

## 🖥️ Logfire Integration

FastSocket integrates with **Logfire** to provide real-time log management and visualization, enhancing observability
and facilitating efficient debugging.

- **Logfire Project URL
  **: [https://logfire.pydantic.dev/seanchatmangpt/fastsocket](https://logfire.pydantic.dev/seanchatmangpt/fastsocket)
- **Features**:
    - Real-time log streaming.
    - Search and filter logs based on severity levels and keywords.
    - Visual dashboards for monitoring log trends and anomalies.

### Accessing Logfire

Navigate to the Logfire project URL to access the log viewer interface. Utilize the CLI commands to manage and interact
with logs seamlessly.

```bash
fs7 log view-logs --lines 100
```

---

## 📈 Performance and Scalability

FastSocket is engineered for high performance and scalability, ensuring efficient handling of a large volume of
real-time events and simultaneous client connections.

### Asynchronous Processing

Leveraging FastAPI's asynchronous capabilities and Socket.IO's non-blocking event handling, FastSocket can manage
numerous concurrent connections without compromising on responsiveness.

### Reactive Streams with RxPY

Implementing ReactiveX (RxPY) allows FastSocket to handle complex event streams with ease, enabling transformations,
filtering, and aggregation of events in a declarative manner. This approach facilitates scalable and maintainable event
processing pipelines.

### Containerization and Orchestration

By containerizing the application with Docker and orchestrating services with Docker Compose, FastSocket ensures
consistent deployment environments and simplifies horizontal scaling across multiple instances.

### Load Balancing

For further scalability, integrating load balancers (e.g., Nginx, HAProxy) can distribute incoming traffic across
multiple FastSocket instances, enhancing performance and reliability.

---

## 📜 Documentation

Comprehensive documentation is available to guide developers through the setup, usage, and extension of FastSocket.

### Sections

- **Getting Started**: Step-by-step instructions to set up and run FastSocket locally.
- **API Reference**: Detailed documentation of all API endpoints, parameters, and responses.
- **CLI Usage**: Guide to utilizing the Typer-powered CLI for server and log management.
- **Event Handling**: Instructions on defining, registering, and managing event handlers using AsyncAPI.
- **Logging**: Overview of Loguru configuration and Logfire integration for log management.
- **Deployment**: Strategies and configurations for deploying FastSocket using Docker and Docker Compose.
- **Testing**: Guidelines for running and extending the test suite to ensure application reliability.

### Accessing Documentation

Refer to the [Documentation](https://linktodocumentation) for in-depth guides and references.

---

## 🤖 Example Usage

### Generating Event Handlers and Vue Pages

Utilize the CLI to automate the generation of backend handlers and frontend components based on your AsyncAPI
specification.

```bash
# Generate Python event handlers
fs7 handlers --asyncapi-file asyncapi.yaml --output-dir src/fastsocket/events

# Generate Vue.js frontend components
fs7 pages --asyncapi-file asyncapi.yaml --output-dir nuxt-app/pages
```

### Triggering an Event via API

Send a POST request to trigger an event and observe the real-time handling.

```bash
curl -X POST "http://localhost:8000/api/events" \
     -H "Content-Type: application/json" \
     -H "api_key: your_api_key" \
     -d '{
           "name": "user_signed_up",
           "payload": {
               "user_id": "12345",
               "email": "user@example.com"
           }
         }'
```

### Viewing Logs in Real-Time

Tail the log file to monitor server operations and event handling in real-time.

```bash
fs7 log tail-logs
```

---

## 📖 Lessons Learned

Developing FastSocket provided profound insights into integrating multiple cutting-edge technologies to build a
cohesive, scalable, and efficient real-time application framework.

### Key Learnings

1. **Event-Driven Architecture**: The integration of AsyncAPI with Socket.IO and FastAPI underscores the importance of
   standardized event definitions in maintaining consistency and scalability.

2. **Asynchronous Programming**: Leveraging Python's `async` and `await` keywords in FastAPI and Socket.IO enhances the
   application's ability to handle numerous concurrent connections efficiently.

3. **Reactive Programming Paradigms**: Implementing RxPY introduced a robust framework for managing complex event
   streams, enabling responsive and maintainable data flows.

4. **Automated Code Generation**: Utilizing templating engines like Jinja2 in conjunction with AsyncAPI automates
   repetitive coding tasks, reducing errors and accelerating development cycles.

5. **Structured Logging**: Adopting Loguru for logging provided an effective mechanism for capturing detailed,
   structured logs, essential for monitoring and debugging.

6. **CLI Development**: Building a CLI with Typer streamlined server management and operational workflows, enhancing
   developer productivity and operational efficiency.

7. **Containerization**: Docker and Docker Compose facilitated consistent deployment environments, simplifying the
   transition from development to production.

8. **Scalability Considerations**: Designing FastSocket with scalability in mind ensures that it can handle increased
   loads and evolving application demands without compromising performance.

### Challenges Overcome

- **Dynamic Event Handling**: Ensuring that event handlers could be dynamically registered and reloaded required
  meticulous management of module imports and Socket.IO integrations.

- **Data Validation**: Implementing Pydantic models for strict data validation necessitated a thorough understanding of
  schema definitions and their translation from AsyncAPI specifications.

- **Real-Time Log Management**: Integrating Logfire for real-time log viewing involved configuring log streams and
  ensuring seamless communication between the application and the logging platform.

---

## 🧭 Future Work

FastSocket is poised for continual enhancement, with several key areas earmarked for future development:

1. **Enhanced Frontend Dashboard**:
    - Develop a comprehensive Nuxt.js-based dashboard for monitoring events, managing handlers, and visualizing
      real-time data streams.
    - Integrate with Logfire for in-dashboard log analytics and visualization.

2. **Advanced Authentication Mechanisms**:
    - Implement OAuth2 and JWT-based authentication to secure API endpoints and Socket.IO connections.
    - Introduce role-based access controls for granular permission management.

3. **Distributed Event Handling**:
    - Scale event processing across multiple server instances using message brokers like RabbitMQ or Kafka.
    - Implement load balancing and failover strategies to ensure high availability.

4. **GraphQL Integration**:
    - Introduce GraphQL endpoints to provide flexible and efficient data querying capabilities alongside RESTful APIs.

5. **Comprehensive Monitoring and Metrics**:
    - Integrate monitoring tools (e.g., Prometheus, Grafana) to track application performance, event processing times,
      and system health.
    - Provide real-time metrics dashboards for operational insights.

6. **Automated Documentation Generation**:
    - Leverage AsyncAPI and Swagger/OpenAPI specifications to automatically generate comprehensive documentation for
      both backend and frontend components.
    - Implement interactive API explorers for enhanced developer accessibility.

7. **Continuous Integration and Deployment (CI/CD)**:
    - Set up CI/CD pipelines to automate testing, building, and deployment processes, ensuring rapid and reliable
      delivery of updates.

8. **Multi-Tenancy Support**:
    - Enable support for multiple isolated environments within the same FastSocket instance, catering to diverse client
      groups or application segments.

---

## 🧑‍🔬 Academic Insights

The development of FastSocket underscores the intersection of modern web development practices with advanced
architectural patterns and programming paradigms. The integration of **Reactive Programming** through RxPY and *
*Event-Driven Architecture** via AsyncAPI demonstrates the practical application of theoretical concepts in building
scalable and responsive systems.

### Research Implications

- **Scalability and Performance**: FastSocket exemplifies how asynchronous frameworks and reactive programming can be
  harnessed to build systems capable of handling high concurrency with minimal latency.

- **Standardization in Event-Driven Systems**: The adoption of AsyncAPI as a standard for defining event channels and
  messages highlights the importance of standardized specifications in facilitating interoperability and reducing
  integration complexities.

- **Automated Code Generation**: Leveraging templating engines for code generation based on formal specifications (
  AsyncAPI) bridges the gap between design and implementation, fostering consistency and reducing manual coding errors.

- **Reactive Systems**: Incorporating RxPY introduces reactive paradigms into real-time systems, enabling sophisticated
  event processing capabilities that align with modern software engineering principles.

### Potential Areas for Further Study

- **Optimizing Reactive Streams**: Investigate methodologies to optimize event stream processing in high-load scenarios
  using ReactiveX principles.

- **Formal Verification of Event Handlers**: Explore techniques for formally verifying the correctness and reliability
  of dynamically generated event handlers.

- **Enhanced Security Protocols**: Assess and implement advanced security measures within event-driven architectures to
  safeguard against emerging threats.

---

## 📜 References

- **FastAPI Documentation**: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- **Socket.IO Documentation**: [https://socket.io/docs/v4/](https://socket.io/docs/v4/)
- **AsyncAPI Specification**: [https://www.asyncapi.com/docs](https://www.asyncapi.com/docs)
- **Pydantic Documentation**: [https://pydantic-docs.helpmanual.io/](https://pydantic-docs.helpmanual.io/)
- **Typer Documentation**: [https://typer.tiangolo.com/](https://typer.tiangolo.com/)
- **Logfire Documentation**: [https://logfire.pydantic.dev/docs](https://logfire.pydantic.dev/docs)
- **RxPY Documentation**: [https://rxpy.readthedocs.io/en/latest/](https://rxpy.readthedocs.io/en/latest/)
- **Poetry Documentation**: [https://python-poetry.org/docs/](https://python-poetry.org/docs/)
- **Docker Documentation**: [https://docs.docker.com/](https://docs.docker.com/)
- **Docker Compose Documentation**: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
- **Pytest Documentation**: [https://docs.pytest.org/en/stable/](https://docs.pytest.org/en/stable/)
- **Nuxt.js Documentation**: [https://nuxtjs.org/docs/](https://nuxtjs.org/docs/)
- **Vue.js Documentation**: [https://vuejs.org/v2/guide/](https://vuejs.org/v2/guide/)
- **ReactiveX Documentation
  **: [http://reactivex.io/documentation/operators.html](http://reactivex.io/documentation/operators.html)

---

## 📢 Acknowledgments

FastSocket is the culmination of collaborative efforts and the integration of various open-source technologies. Special
thanks to the developers and communities behind FastAPI, Socket.IO, AsyncAPI, Pydantic, Typer, Logfire, and RxPY for
providing the tools and documentation that made this project possible.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🧑‍💻 About the Developer

**Sean Chatman** (He/Him)  
Full Stack Developer specializing in **Front End Generative AI Web Development** with expertise in **TypeScript**, *
*React**, **Vue**, and **Python**.

- **Portfolio**: [https://seanchatmangpt.com](https://seanchatmangpt.com)
- **Email**: [sean@example.com](mailto:sean@example.com)
- **LinkedIn**: [linkedin.com/in/seanchatmangpt](https://linkedin.com/in/seanchatmangpt)
- **GitHub**: [github.com/seanchatmangpt](https://github.com/seanchatmangpt)

---

This comprehensive README encapsulates the technical depth and sophisticated architecture of FastSocket, providing a
clear roadmap for developers, contributors, and stakeholders to understand, utilize, and extend the project. The
emphasis on advanced technologies and architectural principles positions FastSocket as a robust solution for real-time,
event-driven applications.