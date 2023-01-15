from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise  # type: ignore

from etherealink.config import get_settings


def orm_init(app: FastAPI) -> None:
    # tortoise orm doesn't recognize 'postgresql' as a valid db scheme
    # replace the scheme name as a hacky fix
    db_url = get_settings().db_url.replace('postgresql', 'postgres')
    register_tortoise(
        app,
        db_url=db_url,
        modules={"models": ["etherealink.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
