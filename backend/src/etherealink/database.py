from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise  # type: ignore

from etherealink.config import get_settings


def orm_init(app: FastAPI) -> None:
    print(f'{get_settings().db_url=}')
    register_tortoise(
        app,
        db_url=get_settings().db_url,
        modules={"models": ["etherealink.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
