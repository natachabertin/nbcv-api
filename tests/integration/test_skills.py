from tests.db_utils import client
import pytest

def test_create():
    response = client.post(
        "/skills/",
        json={
            "name": "python",
            "level": 9,
            "category": "back-end"
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["name"] == "python"
    assert data["level"] == '9'
    assert data["category"] == "back-end"


def test_get_list():
    response = client.get(f"/skills/")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_get_by_id():
    skill_id = 1
    response = client.get(f"/skills/{skill_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == skill_id


def test_update():
    skill_id = 1
    response = client.patch(
        f"/skills/{skill_id}",
        json={
            "name": "react",
            "level": 4,
            "category": "front-end"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "react"
    assert data["level"] == 4
    assert data["category"] == "front-end"


def test_delete():
    skill_id = 1
    response = client.delete("/skills/{skill_id}")
    assert response.status_code == 200, response.text

    response = client.get(f"/skills/{skill_id}")
    assert response.status_code == 404, None
