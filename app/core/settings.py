from typing import Any

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )

    APP_NAME: str
    APP_ENV: str
    DEBUG: bool

    API_V1_PREFIX: str
    PORT: int
    HOST: str

    DATABASE_URL: str
    CORS_ORIGINS: str


@field_validator("CORS_ORIGINS", mode="before")
@classmethod
def split_cors(cls, value: Any) -> Any:
    if isinstance(value, str):
        return [origin.strip() for origin in value.split(",") if origin.strip()]
    return value


settings = Settings()
