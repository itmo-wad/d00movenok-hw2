from typing import Any

from argon2 import PasswordHasher  # type: ignore
from bson import ObjectId
from config import app_config  # type: ignore
from db.mongo import AsyncIOMotorClient  # type: ignore
from models.auth import UserInfo  # type: ignore

hasher = PasswordHasher()


def _hash_password(password: str) -> str:
    hash: str = hasher.hash(password)
    return hash


def _validate_password(password: str, hash: str) -> bool:
    try:
        ok: bool = hasher.verify(hash, password)
        return ok
    except:
        return False


def _mongo_obj_to_profile(obj: dict[str, Any]) -> UserInfo:
    return UserInfo(
        id=str(obj["_id"]),
        login=obj["login"],
        avatar=obj["avatar"],
        description=obj["description"],
    )


async def find_user_by_login(
    db: AsyncIOMotorClient,
    login: str,
) -> UserInfo | None:
    result = await db[app_config.mongo_db].users.find_one({"login": login})
    if result is None:
        return None

    return _mongo_obj_to_profile(result)


async def find_user_by_login_and_password(
    db: AsyncIOMotorClient, login: str, password: str
) -> UserInfo | None:
    result = await db[app_config.mongo_db].users.find_one({"login": login})
    if result is None:
        return None

    is_pass_valid = _validate_password(password, result["hash"])
    if not is_pass_valid:
        return None

    return _mongo_obj_to_profile(result)


async def find_user_by_id(db: AsyncIOMotorClient, id: str) -> UserInfo | None:
    result = await db[app_config.mongo_db].users.find_one({"_id": ObjectId(id)})
    if result is None:
        return None

    return _mongo_obj_to_profile(result)


async def create_user(db: AsyncIOMotorClient, login: str, password: str) -> UserInfo:
    password_hash = _hash_password(password)
    result = await db[app_config.mongo_db].users.insert_one(
        {"login": login, "hash": password_hash, "avatar": "", "description": ""}
    )
    return UserInfo(id=str(result.inserted_id), login=login, avatar="", description="")
