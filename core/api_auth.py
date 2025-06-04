from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.logger import auth_logger as logger


@asynccontextmanager
async def fastapi_lifespan(app: FastAPI):

    logger.info('=== Auth service started ===')

    yield

    logger.info('=== Auth service stopped ===')


app = FastAPI(
    title="authorization-service",
    lifespan=fastapi_lifespan
)