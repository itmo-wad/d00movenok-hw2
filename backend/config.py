import uuid

from pydantic import BaseModel, BaseSettings, Field


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "uvicorn"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        LOGGER_NAME: {
            "handlers": ["default"],
            "level": LOG_LEVEL,
        },
    }


class AppConfig(BaseSettings):
    mongo_user: str = Field(..., env="MONGO_USER")
    mongo_pass: str = Field(..., env="MONGO_PASS")
    mongo_host: str = Field(default="mongo", env="MONGO_HOST")
    mongo_port: int = Field(default=27017, env="MONGO_PORT")
    mongo_db: str = Field(default="admin", env="MONGO_DB")
    mongo_min_conndection: int = Field(default=10, env="MONGO_MIN_CONNECTIONS")
    mongo_max_conndection: int = Field(default=50, env="MONGO_MAX_CONNECTIONS")
    secret: str = Field(default=uuid.uuid4().hex, env="APP_SECRET")
    debug: bool = Field(default=False, env="DEBUG")


log_config = LogConfig()
app_config = AppConfig()
