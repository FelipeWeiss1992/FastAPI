from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://fastapi:1234@localhost:5433/postgres"
    DBBaseModel = declarative_base()
    class config():
        case_sensitive = True

class Config:
    case_sensitive = True
    
settings = Settings()