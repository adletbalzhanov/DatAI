from pydantic.v1 import BaseSettings


class Config(BaseSettings):
    OPENAI_API_KEY: str = "default"
    DATAI_API_KEY: str = "default"


def get_current_config() -> Config:
    return Config()


current_config = get_current_config()
