import logging

from fastapi import FastAPI
from fastapi_socketio import SocketManager  # type: ignore

logger = logging.getLogger("uvicorn")


class SocketIO:
    manager: SocketManager = None


socketio = SocketIO()


def init_socketio(app: FastAPI) -> None:
    logger.info("Initializing socketio...")
    socketio.manager = SocketManager(app=app, mount_location="/ws")
    logger.info("Socketio initialized")
