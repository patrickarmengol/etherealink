from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    env_name: str = 'local'
    base_url: str = 'http://localhost:5000'
    db_url: str = 'sqlite://:memory:'

    class Config(BaseSettings.Config):  # https://github.com/pydantic/pydantic/issues/4223
        env_file = '.env'


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    # print(f'loading settings for: {settings.env_name}')
    return settings
