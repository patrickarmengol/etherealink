from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from etherealink.config import get_settings


def orm_init(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=get_settings().db_url,
        modules={"models": ["etherealink.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
