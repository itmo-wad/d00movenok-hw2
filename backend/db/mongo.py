from motor.motor_asyncio import AsyncIOMotorClient  # type: ignore


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.client
