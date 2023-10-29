from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    ENCRYPTION_KEY: str

    @property
    def get_database_url(self):
        return (f"postgresql+asyncpg://{self.DB_USER}:"
                f"{self.DB_PASS}@"
                f"{self.DB_HOST}:"
                f"{self.DB_PORT}/"
                f"{self.DB_NAME}")


settings = Settings()
