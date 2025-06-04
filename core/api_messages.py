from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.logger import messages_logger as logger


@asynccontextmanager
async def fastapi_lifespan(app: FastAPI):

    logger.info('=== Messages service started ===')

    yield

    logger.info('=== Messages service stopped ===')


app = FastAPI(
    title="messages-service",
    lifespan=fastapi_lifespan
)