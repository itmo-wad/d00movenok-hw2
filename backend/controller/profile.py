from controller.middleware.auth import auth_required  # type: ignore
from db.mongo import AsyncIOMotorClient, get_database  # type: ignore
from fastapi import APIRouter, Depends, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.auth import UserInfo  # type: ignore
from service.auth import find_user_by_id  # type: ignore

router = APIRouter()


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
