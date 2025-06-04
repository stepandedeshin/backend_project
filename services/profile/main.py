import uvicorn

from core.api_messages import app
from core.logger import profile_logger as logger
from app.router import router as profile_router


app.include_router(profile_router)


if __name__ == "__main__":
    try:
        uvicorn.run(
            app=app,
            host="localhost",
            port=5006
        )
    except KeyboardInterrupt:
        logger.info('Exit profile srvice')
