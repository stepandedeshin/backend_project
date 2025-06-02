import uvicorn

from core.api_auth_service import app
from core.logger import auth_logger as logger


if __name__ == "__main__":
    try:
        uvicorn.run(
            app=app,
            host="localhost",
            port=7000
        )
    except KeyboardInterrupt:
        logger.info('Exit auth_srvice')
