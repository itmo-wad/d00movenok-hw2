import logging
import os

from config import app_config  # type: ignore
from controller.middleware.auth import auth_required  # type: ignore
from db.mongo import AsyncIOMotorClient, get_database  # type: ignore
from fastapi import APIRouter, Depends, File, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse, JSONResponse
from models.auth import UserInfo  # type: ignore
from models.profile import NewDescription, NewPassword  # type: ignore
from models.response import Error, Message  # type: ignore
from service.auth import find_user_by_id  # type: ignore
from service.profile import update_description  # type: ignore
from service.profile import set_avatar, update_password

router = APIRouter()
logger = logging.getLogger("uvicorn")


@router.get("", dependencies=[Depends(auth_required)])
async def profile(
    request: Request,
    db: AsyncIOMotorClient = Depends(get_database),
) -> UserInfo:
    user = await find_user_by_id(db, request.session["id"])
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(user),
    )


@router.put("/description", dependencies=[Depends(auth_required)])
async def edit_description(
    description: NewDescription,
    request: Request,
    db: AsyncIOMotorClient = Depends(get_database),
) -> Error | Message:
    ok = await update_description(db, request.session["id"], description.description)
    if not ok:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=jsonable_encoder(Error(error="Something went wrong")),
        )

    logger.debug("Changed description for user id:" + request.session["id"])

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(Message(message="Succesfully changed description")),
    )


@router.put("/password", dependencies=[Depends(auth_required)])
async def edit_password(
    passwords: NewPassword,
    request: Request,
    db: AsyncIOMotorClient = Depends(get_database),
) -> Error | Message:
    ok = await update_password(
        db,
        request.session["id"],
        passwords.old_password,
        passwords.new_password,
    )
    if not ok:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder(Error(error="Bad password")),
        )

    logger.debug("Changed password for user id:" + request.session["id"])

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(Message(message="Succesfully changed password")),
    )


@router.get("/avatar", dependencies=[Depends(auth_required)])
async def get_avatar(
    id: str,
) -> Error | Message:
    if id.find(".") != -1:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(Error(error="Path traversal detected!")),
        )
    path = os.path.join(app_config.avatars_storage, id)
    return FileResponse(path)


@router.put("/avatar", dependencies=[Depends(auth_required)])
async def update_avatar(
    request: Request,
    avatar: bytes = File(),
    db: AsyncIOMotorClient = Depends(get_database),
) -> Error | Message:
    id = request.session["id"]

    ok = await set_avatar(db, id, avatar)
    if not ok:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder(Error(error="Something went wrong")),
        )

    logger.debug("Changed avatar for user id:" + request.session["id"])
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(Message(message="Successfully changed an avatar")),
    )
