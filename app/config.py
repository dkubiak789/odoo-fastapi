from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    odoo_url: str
    odoo_db: str
    odoo_username: str
    odoo_password: str

    class Config:
        env_file = ".env"


settings = Settings()
