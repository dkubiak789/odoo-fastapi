from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Odoo FastAPI Integration"
    api_v1_prefix: str = "/api/v1"
    odoo_url: str
    odoo_db: str
    odoo_username: str
    odoo_password: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
