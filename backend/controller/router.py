from controller import auth, healthcheck, profile  # type: ignore
from fastapi import APIRouter

router = APIRouter()
router.include_router(auth.router, tags=["auth"])
router.include_router(profile.router, tags=["profile"])
router.include_router(healthcheck.router, tags=["healthcheck"])
