import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from unittest.mock import MagicMock, AsyncMock
from app.main import app
from app.database import get_db


def make_mock_session():
    mock_session = MagicMock()
    mock_session.execute = AsyncMock()
    mock_session.commit = AsyncMock()
    mock_session.refresh = AsyncMock()  # must be AsyncMock
    mock_session.delete = AsyncMock()   # must be AsyncMock
    mock_session.add = MagicMock()
    return mock_session


@pytest.fixture
def mock_session():
    return make_mock_session()


@pytest_asyncio.fixture
async def client(mock_session):
    async def override_get_db():
        yield mock_session

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        yield ac

    app.dependency_overrides.clear()