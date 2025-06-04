import uvicorn

from core.api_friends import app
from core.logger import friends_logger as logger


if __name__ == "__main__":
    try:
        uvicorn.run(
            app=app,
            host="localhost",
            port=5004
        )
    except KeyboardInterrupt:
        logger.info('Exit friends service')
