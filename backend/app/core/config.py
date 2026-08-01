from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "AI Software Engineer Assistant"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = (
        "An AI-powered assistant that analyzes software repositories."
    )
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str   

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int 

    GEMINI_API_KEY: str
     
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
settings = Settings()


    