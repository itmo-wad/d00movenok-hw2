from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def profile() -> str:
    return "ok"
