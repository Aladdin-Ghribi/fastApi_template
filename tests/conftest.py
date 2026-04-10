import os
from typing import Generator

import pytest
from fastapi.testclient import TestClient

os.environ["APP_ENV"] = "test"


from app.main import app  # noqa: E402


@pytest.fixture()
def client() -> TestClient:
    return TestClient(app)
