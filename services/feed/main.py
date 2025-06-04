import uvicorn

from core.api_feed import app
from core.logger import feed_logger as logger


if __name__ == "__main__":
    try:
        uvicorn.run(
            app=app,
            host="localhost",
            port=5003
        )
    except KeyboardInterrupt:
        logger.info('Exit feed service')
