import logging

from config import app_config  # type: ignore
from db.mongo import db  # type: ignore
from motor.motor_asyncio import AsyncIOMotorClient  # type: ignore

logger = logging.getLogger("uvicorn")


async def connect_to_mongo() -> None:
    logger.info("Connecting to database...")
    db.client = AsyncIOMotorClient(
        f"mongodb://{app_config.mongo_user}:{app_config.mongo_pass}@{app_config.mongo_host}:{app_config.mongo_port}/{app_config.mongo_db}",
        maxPoolSize=app_config.mongo_max_conndection,
        minPoolSize=app_config.mongo_min_conndection,
    )
    await db.client[app_config.mongo_db].command("ping")
    logger.info("Database connected！")


async def close_mongo_connection() -> None:
    logger.info("Closing database connection...")
    db.client.close()
    logger.info("Database closed！")
