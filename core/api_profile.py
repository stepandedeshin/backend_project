from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.logger import profile_logger as logger


@asynccontextmanager
async def fastapi_lifespan(app: FastAPI):

    logger.info('=== Profile service started ===')

    yield

    logger.info('=== Profile service stopped ===')


app = FastAPI(
    title="profile-service",
    lifespan=fastapi_lifespan
)