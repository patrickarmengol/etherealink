import string
from datetime import datetime

from pydantic import AnyHttpUrl, BaseModel, validator


class URLBase(BaseModel):
    target_url: AnyHttpUrl


class URLSettings(BaseModel):
    clicks_left: int | None
    expiry: datetime | None


class URLCreate(URLBase, URLSettings):
    pass


class URLCustom(URLCreate):
    custom_key: str | None

    @validator('custom_key')
    def check_custom(cls, v: str):
        # return if null
        if v is None:
            return v
        # alphanum or underscore or dash
        allowed = string.ascii_letters + string.digits + '-_'
        if not (1 <= len(v) <= 40) or not all(c in allowed for c in v):
            raise ValueError(
                'custom_key length is between 1 and 40 and can only contain letters + digits + dashes + underscores')
        return v


class URLInfo(URLCreate):
    url_key: str
    admin_key: str

    class Config:
        orm_mode = True
