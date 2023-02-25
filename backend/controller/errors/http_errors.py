from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from models.response import Error  # type: ignore
from starlette.requests import Request  # type: ignore
from starlette.responses import JSONResponse  # type: ignore


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        jsonable_encoder(Error(error=exc.detail)), status_code=exc.status_code
    )
