import os
from dotenv import load_dotenv
from functools import lru_cache
load_dotenv(".env")

@lru_cache()
class Settings:
    HOST: str = os.getenv("HOST", "localhost")
    PORT: int = int(os.getenv("PORT", 8000))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+psycopg2://user:password@localhost/dbname") # postgresql+psycopg2://user:password@localhost/dbname
    MONGO_URL: str = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "test")
    ALLOWED_HOSTS: list = os.getenv("ALLOWED_HOSTS", "").split(",") if os.getenv("ALLOWED_HOSTS") else []
    API_VERSION: str = os.getenv("API_VERSION", "v1")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    CORS_ORIGINS: list = os.getenv("CORS_ORIGINS", "").split(",") if os.getenv("CORS_ORIGINS") else []
    RATE_LIMIT: str = os.getenv("RATE_LIMIT", "100/hour")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRATION: int = int(os.getenv("JWT_EXPIRATION", 3600))
    EMAIL_HOST: str = os.getenv("EMAIL_HOST", "smtp.example.com")
    EMAIL_PORT: int = int(os.getenv("EMAIL_PORT", 587))
    EMAIL_USE_TLS: bool = os.getenv("EMAIL_USE_TLS", "True").lower() in ("true", "1", "yes")
    EMAIL_HOST_USER: str = os.getenv("EMAIL_HOST_USER", "")
    EMAIL_HOST_PASSWORD: str = os.getenv("EMAIL_HOST_PASSWORD", "")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    SENTRY_DSN: str = os.getenv("SENTRY_DSN", "")
    LOGGING_CONFIG: dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            }
        },
        "loggers": {
            "uvicorn.error": {"level": LOG_LEVEL, "handlers": ["console"], "propagate": True},
            "uvicorn.access": {"level": LOG_LEVEL, "handlers": ["console"], "propagate": True},
        },
    }

    @classmethod
    def from_env(cls):
        return cls()

    @property
    def database_url(self):
        return self.DATABASE_URL    
    @property
    def email_settings(self):
        return {
            "host": self.EMAIL_HOST,
            "port": self.EMAIL_PORT,
            "use_tls": self.EMAIL_USE_TLS,
            "user": self.EMAIL_HOST_USER,
            "password": self.EMAIL_HOST_PASSWORD,
        }  
    @property
    def redis_url(self):
        return self.REDIS_URL
    
setting = Settings()