from pydantic import SecretStr
from pydantic.v1 import BaseSettings


class BaseConfig(BaseSettings):
    # database settings
    MYSQL_USER: str = "user"
    MYSQL_PASS: SecretStr = SecretStr("password")
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_DB: str = "db"
    OPENAI_API_KEY: SecretStr = SecretStr(
        "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"
    )

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return (
            f"mysql+asyncmy://{self.MYSQL_USER}:{self.MYSQL_PASS}"
            f"@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
        )


class ProductionConfig(BaseConfig):
    pass


def get_current_config() -> BaseConfig:
    return ProductionConfig()


current_config = get_current_config()
