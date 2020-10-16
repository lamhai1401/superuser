from typing import Callable
from fastapi import FastAPI
from loguru import logger
from src.db.mysql import init_orm, close_orm


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await init_orm()
    return start_app


def create_end_app_handler(app: FastAPI) -> Callable:
    async def end_app() -> None:
        await close_orm()
    return end_app
