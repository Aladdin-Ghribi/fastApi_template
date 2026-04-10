from collections.abc import AsyncGenerator

from app.db.session import async_session_local


async def get_db() -> AsyncGenerator:
    async with async_session_local() as session:
        yield session
