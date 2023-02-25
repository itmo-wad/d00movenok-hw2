import logging
from logging.config import dictConfig

from config import LogConfig  # type: ignore
from controller.errors.http_errors import http_error_handler  # type: ignore
from controller.router import router as api_router  # type: ignore
from fastapi import FastAPI, HTTPException

# from backend.events.fastapi import create_start_app_handler, create_stop_app_handler

dictConfig(LogConfig().dict())
logger = logging.getLogger("uvicorn")


def get_application() -> FastAPI:
    application = FastAPI(title="WAD-HW2", debug=True, version="0.1")

    application.add_exception_handler(HTTPException, http_error_handler)
    # application.add_event_handler("startup", create_start_app_handler(application))
    # application.add_event_handler("shutdown", create_stop_app_handler(application))

    application.include_router(api_router)

    return application


app = get_application()

logger.info("Open http://127.0.0.1:8000/docs to see Swagger API Documentation.")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
