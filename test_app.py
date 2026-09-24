from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Hello, Flask CI/CD!"


def test_about():
    client = app.test_client()

    response = client.get("/about")

    assert response.status_code == 200
    assert response.data == b"This is my Flask project."
