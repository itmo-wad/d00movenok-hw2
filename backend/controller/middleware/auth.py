from db.mongo import AsyncIOMotorClient, get_database  # type: ignore
from fastapi import Depends, HTTPException, Request, status
from service.auth import find_user_by_id  # type: ignore


async def auth_required(
    request: Request, db: AsyncIOMotorClient = Depends(get_database)
) -> None:
    id = request.session.get("id", None)
    user = await find_user_by_id(db, id)
    if user == None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Unauthorized",
        )

    return
