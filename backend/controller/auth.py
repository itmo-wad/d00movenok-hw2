import logging

from controller.middleware.auth import auth_required  # type: ignore
from db.mongo import AsyncIOMotorClient, get_database  # type: ignore
from fastapi import APIRouter, Depends, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.auth import AuthData, UserInfo  # type: ignore
from models.response import Error, Message  # type: ignore
from service.auth import find_user_by_login  # type: ignore
from service.auth import create_user, find_user_by_login_and_password

router = APIRouter()
logger = logging.getLogger("uvicorn")


@router.post("/signin")
async def signin(
    body: AuthData,
    request: Request,
    db: AsyncIOMotorClient = Depends(get_database),
) -> Error | UserInfo:
    user = await find_user_by_login_and_password(db, body.login, body.password)
    if not user:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content=jsonable_encoder(Error(error="Wrong credentials!")),
        )

    logger.debug("Signed in: " + body.login)
    request.session["id"] = user.id
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(user),
    )


@router.post("/signup")
async def signup(
    body: AuthData,
    request: Request,
    db: AsyncIOMotorClient = Depends(get_database),
) -> Error | UserInfo:
    user = await find_user_by_login(db, body.login)
    if user:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder(Error(error="Username already taken")),
        )

    user = await create_user(db, body.login, body.password)
    logger.debug("Created new user: " + body.login)
    request.session["id"] = user.id
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(user),
    )


@router.post("/signout", dependencies=[Depends(auth_required)])
async def logout(request: Request) -> Message:
    logger.debug("Signed out: " + request.session.get("id", "-"))
    request.session["id"] = ""
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(Message(message="logged out")),
    )
