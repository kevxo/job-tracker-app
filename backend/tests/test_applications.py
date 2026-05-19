import pytest
from unittest.mock import MagicMock
from datetime import date, datetime
from app.models.application import Application


def make_mock_app(**kwargs):
    mock = MagicMock(spec=Application)
    mock.id = kwargs.get("id", 1)
    mock.company = kwargs.get("company", "Google")
    mock.role = kwargs.get("role", "Software Engineer I")
    mock.status = kwargs.get("status", "applied")
    mock.date_applied = kwargs.get("date_applied", date(2026, 5, 1))
    mock.salary_min = kwargs.get("salary_min", None)
    mock.salary_max = kwargs.get("salary_max", None)
    mock.job_url = kwargs.get("job_url", None)
    mock.notes = kwargs.get("notes", None)
    mock.contact_name = kwargs.get("contact_name", None)
    mock.contact_email = kwargs.get("contact_email", None)
    mock.created_at = kwargs.get("created_at", datetime(2026, 5, 1))
    mock.updated_at = kwargs.get("updated_at", None)
    return mock


@pytest.mark.asyncio
async def test_root(client):
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Job Tracker API is running"}


@pytest.mark.asyncio
async def test_get_applications(client, mock_session):
    mock_app = make_mock_app()
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [mock_app]
    mock_session.execute.return_value = mock_result

    response = await client.get("/applications/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_create_application(client, mock_session):
    from datetime import datetime

    async def mock_refresh(obj):
        obj.id = 1
        obj.created_at = datetime(2026, 5, 1)
        obj.updated_at = None

    mock_session.refresh = mock_refresh

    response = await client.post("/applications/", json={
        "company": "Google",
        "role": "Software Engineer I",
        "status": "applied",
        "date_applied": "2026-05-01",
    })
    assert response.status_code == 201
    assert response.json()["company"] == "Google"


@pytest.mark.asyncio
async def test_get_single_application(client, mock_session):
    mock_app = make_mock_app()
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = mock_app
    mock_session.execute.return_value = mock_result

    response = await client.get("/applications/1")
    assert response.status_code == 200
    assert response.json()["company"] == "Google"


@pytest.mark.asyncio
async def test_get_nonexistent_application(client, mock_session):
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = None
    mock_session.execute.return_value = mock_result

    response = await client.get("/applications/999999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_update_application(client, mock_session):
    mock_app = make_mock_app(status="interview")
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = mock_app
    mock_session.execute.return_value = mock_result

    response = await client.put("/applications/1", json={
        "company": "Apple",
        "role": "Software Engineer I",
        "status": "interview",
        "date_applied": "2026-05-01",
    })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_application(client, mock_session):
    mock_app = make_mock_app()
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = mock_app
    mock_session.execute.return_value = mock_result

    response = await client.delete("/applications/1")
    assert response.status_code == 204


@pytest.mark.asyncio
async def test_filter_by_status(client, mock_session):
    mock_app = make_mock_app(status="applied")
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [mock_app]
    mock_session.execute.return_value = mock_result

    response = await client.get("/applications/?status=applied")
    assert response.status_code == 200