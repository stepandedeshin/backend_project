import uvicorn

from core.api_auth import app
from core.logger import auth_logger as logger


if __name__ == "__main__":
    try:
        uvicorn.run(
            app=app,
            host="localhost",
            port=5002
        )
    except KeyboardInterrupt:
        logger.info('Exit auth service')
