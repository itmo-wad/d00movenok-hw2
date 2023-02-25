from fastapi import APIRouter

router = APIRouter()


@router.get("/api/healthcheck")
def signup():
    return "ok"
