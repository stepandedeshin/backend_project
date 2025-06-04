from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.logger import friends_logger as logger


@asynccontextmanager
async def fastapi_lifespan(app: FastAPI):

    logger.info('=== Friends service started ===')

    yield

    logger.info('=== Friends service stopped ===')


app = FastAPI(
    title="friends-service",
    lifespan=fastapi_lifespan
)