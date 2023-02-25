import logging
from logging.config import dictConfig

from config import app_config, log_config  # type: ignore
from controller.errors.http_errors import http_error_handler  # type: ignore
from controller.router import router as api_router  # type: ignore
from db.mongo_utils import close_mongo_connection  # type: ignore
from db.mongo_utils import connect_to_mongo
from fastapi import FastAPI, HTTPException
from starlette.middleware.sessions import SessionMiddleware  # type: ignore

dictConfig(log_config.dict())
logger = logging.getLogger("uvicorn")


def get_application() -> FastAPI:
    application = FastAPI(title="WAD-HW2", debug=app_config.debug, version="0.1")
    application.add_middleware(
        SessionMiddleware, max_age=600, secret_key=app_config.secret
    )

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_event_handler("startup", connect_to_mongo)
    application.add_event_handler("shutdown", close_mongo_connection)

    application.include_router(api_router, prefix="/api")

    return application


app = get_application()

logger.info("Open http://127.0.0.1:8000/docs to see Swagger API Documentation.")

if __name__ == "__main__":
    import uvicorn  # type: ignore

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
