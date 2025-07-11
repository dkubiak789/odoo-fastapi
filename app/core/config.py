from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings class that handles configuration.

    This class defines all configuration parameters for the application.
    It automatically reads values from environment variables or .env file.
    Environment variables take precedence over .env file values.
    """

    app_name: str = "Odoo FastAPI Integration"
    api_v1_prefix: str = "/api/v1"
    odoo_url: str
    odoo_db: str
    odoo_username: str
    odoo_password: str
    secret_key: str = Field(..., env="SECRET_KEY")

    class Config:
        """
        Configuration for the Settings class.

        Specifies that settings should be read from a .env file
        in addition to environment variables.
        """

        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    """
    Create and return a cached instance of the Settings class.

    The lru_cache decorator ensures that the settings are only loaded once
    and reused for subsequent calls, improving performance.

    Returns:
        Settings: Application settings instance
    """
    return Settings()


# Create a global settings instance
settings = get_settings()
