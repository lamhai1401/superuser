import logging
import sys
import os
from typing import List
from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret
from .logging import InterceptHandler

API_PREFIX = "/api"
JWT_TOKEN_PREFIX = "Token"  # noqa: S105 在做用户校验时，需要把这个前缀加上，并加空格
VERSION = "1.0.0"
config = Config(".env")
DEBUG: bool = config("DEBUG", cast=bool, default=False)

# db config
DATABASE_URL: str = config("DB_CONNECTION", cast=str) or os.getenv("DB_CONNECTION")  # noqa: E501
HOST: str = config("HOST", cast=str, default="127.0.0.1") or os.getenv("HOST")  # noqa: E501
PORT: int = int(os.getenv("PORT")) if "PORT" in os.environ else config("PORT", cast=int, default=3306)  # noqa: E501
USER: str = config("USER", cast=str, default="username") or os.getenv("USER")
PWD: str = config("PWD", cast=str, default="password") or os.getenv("PWD")
DB: str = config("DB", cast=str, default="db") or os.getenv("DB")

# auth
SECRET_KEY: Secret = os.getenv("SECRET_KEY") or config("SECRET_KEY", cast=Secret)
ALGORITHM: str = os.getenv("ALGORITHM") or config("ALGORITHM", cast=str, default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=30) or int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# project info
PROJECT_NAME: str = config(
    "PROJECT_NAME",
    default="FastAPI example application"
)
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default=""
)

# logging configuration
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
