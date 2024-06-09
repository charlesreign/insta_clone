from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    FRONT_END_BASE_URL: str
    SQLALCHEMY_DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"


env = Settings()
