from tests.utils import client
import pytest

def test_create():
    response = client.post(
        "/users/",
        json={
            "username": "jdoe",
            "email": "jdoe@example.com",
            "password": "jdoepwd"
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["username"] == "jdoe"
    assert data["email"] == "jdoe@example.com"
    assert data["password"] == "jdoepwd"


def test_get_list():
    response = client.get(f"/users/")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_get_by_id():
    user_id = 1
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == user_id


@pytest.mark.skip(reason="Not implemented yet.")
def test_update():
    user_id = 1
    response = client.put(
        "/users/{user_id}",
        json={
            "email": "another@ema.il"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "another@ema.il"

@pytest.mark.skip(reason="Not implemented yet.")
def test_delete():
    user_id = 1
    response = client.delete("/users/{user_id}")

    assert response.status_code == 200, response.text
    data = response.json()

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404, None
