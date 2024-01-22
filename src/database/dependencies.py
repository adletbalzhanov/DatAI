from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from starlette.requests import Request

from src.config import current_config


class DatabaseState:
    def __init__(self):
        self.engine = create_async_engine(current_config.SQLALCHEMY_DATABASE_URI)
        self.session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
            self.engine
        )


async def get_db_session(request: Request) -> AsyncSession:
    async with request.app.state.database.session_maker() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()
