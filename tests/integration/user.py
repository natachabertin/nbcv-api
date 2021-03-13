from tests.utils import client


def test_create_user():
    response = client.post(
        "/users/",
        json={
            "username": "deadpool",
            "email": "deadpool@example.com",
            "password": "chimichangas4life"
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert "id" not in data
    user_id = 1

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert data["id"] == user_id
