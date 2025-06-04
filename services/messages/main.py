import uvicorn

from core.api_messages import app
from core.logger import messages_logger as logger


if __name__ == "__main__":
    try:
        uvicorn.run(
            app=app,
            host="localhost",
            port=5005
        )
    except KeyboardInterrupt:
        logger.info('Exit messages srvice')
