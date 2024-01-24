from pydantic.v1 import BaseSettings


class Config(BaseSettings):
    MYSQL_USER: str = "default"
    MYSQL_PASS: str = "default"
    MYSQL_HOST: str = "default"
    MYSQL_PORT: int = 0
    MYSQL_DB: str = "default"
    OPENAI_API_KEY: str = "default"
    DATAI_API_KEY: str = "default"

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return (
            f"mysql+mysqlconnector://{self.MYSQL_USER}:{self.MYSQL_PASS}"
            f"@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
        )


def get_current_config() -> Config:
    return Config()


current_config = get_current_config()
