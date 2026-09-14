from __future__ import annotations

from importlib.metadata import version as installed_version
from typing import Any

from fastapi.testclient import TestClient

from app.main import app


def test_health_endpoint_structure() -> None:
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    data: dict[str, Any] = response.json()
    assert data["status"] == "healthy"
    assert "version" in data
    assert "model" in data and "providers" in data["model"]
    assert "vectordb" in data and "provider" in data["vectordb"]


def test_health_reports_installed_version() -> None:
    """The served version must equal the installed distribution version.

    Asserting presence alone let the hardcoded __version__ drift a full major
    version behind pyproject.toml while CI stayed green.
    """
    client = TestClient(app)
    data: dict[str, Any] = client.get("/health").json()
    assert data["version"] == installed_version("rag-benchmarking")


def test_openapi_reports_installed_version() -> None:
    """The same value is advertised by /openapi.json, Swagger and ReDoc."""
    client = TestClient(app)
    schema: dict[str, Any] = client.get("/openapi.json").json()
    assert schema["info"]["version"] == installed_version("rag-benchmarking")
