import secrets
import string


async def create_random_key(length: int = 5) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))
