from pydantic import SecretStr
from pydantic.v1 import BaseSettings


class BaseConfig(BaseSettings):
    # database settings
    MYSQL_USER: str = "default"
    MYSQL_PASS: SecretStr = SecretStr("default")
    MYSQL_HOST: str = "default"
    MYSQL_PORT: int = 0
    MYSQL_DB: str = "default"
    OPENAI_API_KEY: SecretStr = SecretStr("default")

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return (
            f"mysql+mysqlconnector://{self.MYSQL_USER}:{self.MYSQL_PASS}"
            f"@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
        )


class ProductionConfig(BaseConfig):
    pass


def get_current_config() -> BaseConfig:
    return ProductionConfig()


current_config = get_current_config()
