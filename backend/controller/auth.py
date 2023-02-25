from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/api/signin")
def signin():
    return JSONResponse(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        content="Not implemented yet",
    )


@router.post("/api/signup")
def signup():
    return JSONResponse(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        content="Not implemented yet",
    )
