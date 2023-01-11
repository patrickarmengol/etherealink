import secrets
import string

from etherealink import crud


async def create_random_key(length: int = 5) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))


async def create_unique_key() -> str:
    key = await create_random_key()
    while await crud.get_db_url_by_url_key(key):
        key = await create_random_key()
    return key
