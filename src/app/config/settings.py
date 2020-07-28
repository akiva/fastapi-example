from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str
    description: str
    version: str = '0.1.0'
    class Config:
        env_file = 'app/.env'
