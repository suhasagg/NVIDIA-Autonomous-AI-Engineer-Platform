from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):
 database_url:str="postgresql+asyncpg://postgres:postgres@localhost:5432/engineer"
 redis_url:str="redis://localhost:6379/0";api_key:str="change-me";tool_mode:str="mock"
 mcp_gateway_url:str="http://localhost:8100";openshell_gateway_url:str="http://localhost:8200"
 model_config=SettingsConfigDict(env_file=".env",extra="ignore")
settings=Settings()
