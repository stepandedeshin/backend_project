from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.logger import feed_logger as logger


@asynccontextmanager
async def fastapi_lifespan(app: FastAPI):

    logger.info('=== Feed service started ===')

    yield

    logger.info('=== Feed service stopped ===')


app = FastAPI(
    title="feed-service",
    lifespan=fastapi_lifespan
)