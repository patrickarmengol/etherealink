from datetime import datetime

from etherealink import keygen, models, schemas


async def create_db_url(url: schemas.URLCustom) -> models.URL:
    url_key = url.custom_key if url.custom_key else await keygen.create_unique_key()
    admin_key = f'{url_key}_{await keygen.create_random_key(8)}'
    db_url = await models.URL.create(
        **url.dict(),
        url_key=url_key,
        admin_key=admin_key,
    )
    return db_url  # maybe use pydantic's .from_orm() to convert here?


async def get_db_url_by_url_key(url_key: str) -> models.URL | None:
    try:
        db_url = await models.URL.get(url_key=url_key)
        return db_url
    except Exception:
        return None


async def update_url_settings(db_url: models.URL, settings: schemas.URLSettings):
    # TODO: find out if there's a better way to update fields for single model obj
    await db_url.update_from_dict(settings.dict(exclude_unset=True))
    await db_url.save()
    return db_url


async def get_db_url_by_admin_key(admin_key: str) -> models.URL | None:
    try:
        db_url = await models.URL.get(admin_key=admin_key)
        return db_url
    except Exception:
        return None


async def delete_url(db_url: models.URL):
    await db_url.delete()
