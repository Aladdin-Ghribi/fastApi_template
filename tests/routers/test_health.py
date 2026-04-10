from fastapi.testclient import TestClient


def test_health(client: TestClient) -> None:
    resp = client.get("/api/v1/health")

    assert resp.status_code == 200
    assert {"status": "ok"}.items() <= resp.json().items()


def test_health_env(client: TestClient) -> None:
    resp = client.get("/api/v1/health")

    assert {"env": "test"}.items() <= resp.json().items()
