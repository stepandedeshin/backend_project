from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.logger import admin_logger as logger


@asynccontextmanager
async def fastapi_lifespan(app: FastAPI):

    logger.info('=== Admin service started ===')

    yield

    logger.info('=== Admin service stopped ===')


app = FastAPI(
    title="admin-service",
    lifespan=fastapi_lifespan
)