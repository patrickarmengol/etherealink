import string
from datetime import datetime

from pydantic import AnyHttpUrl, BaseModel, validator


class URLBase(BaseModel):
    target_url: AnyHttpUrl
    clicks_left: int | None
    expiry: datetime | None


class URLCreate(URLBase):
    custom_key: str | None

    @validator('custom_key')
    def custom_has_alphanum_dash_underscore(cls, v: str):
        # maybe limit length
        allowed = string.ascii_letters + string.digits + '-_'
        if not (1 <= len(v) <= 40) or not all(c in allowed for c in v):
            raise ValueError(
                'custom_key length is between 1 and 40 and can only contain letters + digits + dashes + underscores')
        return v


class URLChange(BaseModel):
    clicks_left: int | None
    expiry: datetime | None


class URLInfo(URLBase):
    url: str
    admin_url: str

    class Config:
        orm_mode = True
