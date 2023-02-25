from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/api/profile")
def profile():
    return JSONResponse(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        content="Not implemented yet",
    )
