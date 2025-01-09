from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_host: str = Field("localhost")
    db_port: int = Field(5432)
    db_name: str = Field("mentor_db")
    db_user: str = Field("user")
    db_password: str = Field("password")

    @property
    def db_asyncpg_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def db_psycopg_url(self):
        return f"postgresql+psycopg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    model_config = SettingsConfigDict(env_file='.env',
                                      case_sensitive=False)


settings = Settings()

