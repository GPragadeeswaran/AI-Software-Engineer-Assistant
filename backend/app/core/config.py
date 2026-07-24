from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "AI Software Engineer Assistant"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = (
        "An AI-powered assistant that analyzes software repositories."
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()