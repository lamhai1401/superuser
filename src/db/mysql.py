from typing import Dict, List, Optional
from tortoise import Tortoise
from src.configs.env import DATABASE_URL, HOST, PORT, DB, PWD, USER
from fastapi import FastAPI
from loguru import logger
# from tortoise.contrib.fastapi import register_tortoise

# Config DB
TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": HOST,
                "port": PORT,
                "user": USER,
                "password": PWD,
                "database": DB
            }
        }
    },
    "apps": {
        "models": {
            "models": ['src.models'],
            "default_connection": "default"
        }
    }
}


async def init_orm() -> None:
    await Tortoise.init(
        config=TORTOISE_ORM,
        # modules={'models': ['__main__']}  # Change here
        # config_file=None,
        # db_url=DATABASE_URL,
        # _create_db=True,
    )
    await Tortoise.generate_schemas()
    logger.info('Tortoise-ORM started, {}, {}'.format(Tortoise._connections, Tortoise.apps))
    # register_tortoise(
    #     app=app,
    #     config=TORTOISE_ORM,
    #     generate_schemas=True,
    #     add_exception_handlers=True
    # )


async def close_orm():
    await Tortoise.close_connections()
    logger.info('Tortoise-ORM shutting down.')
