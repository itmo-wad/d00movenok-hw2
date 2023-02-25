import os

from bson import ObjectId
from config import app_config  # type: ignore
from db.mongo import AsyncIOMotorClient  # type: ignore
from service.auth import _validate_password  # type: ignore
from service.auth import _hash_password, find_user_by_id


async def update_description(db: AsyncIOMotorClient, id: str, description: str) -> bool:
    result = await db[app_config.mongo_db].users.update_one(
        {"_id": ObjectId(id)}, {"$set": {"description": description}}
    )
    return int(result.modified_count) == 1


async def update_password(
    db: AsyncIOMotorClient, id: str, old_password: str, new_password: str
) -> bool:
    result = await db[app_config.mongo_db].users.find_one(
        {"_id": ObjectId(id)},
    )
    is_pass_valid = _validate_password(old_password, result["hash"])
    if not is_pass_valid:
        return False

    new_hash = _hash_password(new_password)
    result = await db[app_config.mongo_db].users.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"hash": new_hash}},
    )
    return int(result.modified_count) == 1


async def set_avatar(db: AsyncIOMotorClient, id: str, file: bytes) -> bool:
    avatars_storage = app_config.avatars_storage
    path = os.path.join(avatars_storage, id)
    with open(path, "wb") as f:
        f.write(file)

    result = await find_user_by_id(db, id)
    if result.avatar:
        return True

    result = await db[app_config.mongo_db].users.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"avatar": True}},
    )

    return int(result.modified_count) == 1
