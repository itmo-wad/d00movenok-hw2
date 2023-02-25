from controller import auth, healthcheck, profile  # type: ignore
from fastapi import APIRouter

router = APIRouter()
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(profile.router, prefix="/profile", tags=["profile"])
router.include_router(healthcheck.router, prefix="/healthcheck", tags=["healthcheck"])
