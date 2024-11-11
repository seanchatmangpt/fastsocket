import sys

import logfire
from loguru import logger

logfire.configure()

# Configure Loguru Logger
logger.remove()  # Remove default logger
logger.add(sys.stdout, format="{time} {level} {message}", level="INFO")
logger.add("logs/debug.log", rotation="1 MB", level="DEBUG", retention="10 days")

logger.configure(handlers=[logfire.loguru_handler()])
# logger.info('Hello, {name}!', name='World')

info = logger.info
debug = logger.debug
error = logger.error
success = logger.success
warning = logger.warning
