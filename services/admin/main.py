import uvicorn

from core.api_admin import app
from core.logger import admin_logger as logger


if __name__ == "__main__":
    try:
        uvicorn.run(
            app=app,
            host="localhost",
            port=5001
        )
    except KeyboardInterrupt:
        logger.info('Exit admin service')
