from typing import Generator, Any
import asyncio
import os

import asyncpg
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from starlette.testclient import TestClient

import settings

# Iteraction with DB
test_engine = create_async_engine(settings.DB_URL_TEST, future=True, echo=True)

test_async_session = sessionmaker(test_engine, expire_on_commit=False, class_=AsyncSession)

CLEAN_TABLES = [
    "users",
]


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session', autouse=True)
async def run_migrations():
    os.system("alembic init migrations")
    os.system('alembic revision --autogenerate -m "test running migrations"')
    os.system("alembic upgrade heads")


@pytest.fixture(scope='session')
async def async_session_test():
    engine = create_async_engine(settings.DB_URL_TEST, future=True, echo=True)
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    yield async_session


@pytest.fixture(scope='session', autouse=True)
async def clean_tables():
    """Clean data in all table before running test funxtion"""
    async with test_async_session() as session:
        async with session.begin():
            for table in CLEAN_TABLES:
                await session.execute(f"""TRUNCATE TABLE {table};""")


async def _get_test_db():
    try:
        yield test_async_session()
    finally:
        pass


@pytest.fixture(scope="function")
async def client() -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    from main import app
    from db.session import get_db

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session")
async def asyncpg_pool():
    pool = await asyncpg.create_pool("".join(settings.DB_URL_TEST.split("+asyncpg")))
    yield pool
    pool.close()


@pytest.fixture
async def get_user_from_database(asyncpg_pool):

    async def get_user_from_database_by_uuid(user_id: str):
        async with asyncpg_pool.acquire() as connection:
            return await connection.fetch("""SELECT * FROM users WHERE user_id = $1;""", user_id)

    return get_user_from_database_by_uuid
