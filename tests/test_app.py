from app import create_app


def test_home_page_loads():
    response = create_app().test_client().get("/")
    assert response.status_code == 200
    assert b"DevOps CI/CD Demo" in response.data


def test_health_endpoint_reports_ok():
    response = create_app().test_client().get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}
