from tests.utils import client
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
    response = client.put(
        f"/skills/{skill_id}",
        json={
            "name": "python",
            "level": 9,
            "category": "back-end"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["level"] == "another@ema.il"

@pytest.mark.skip(reason="Not implemented yet.")
def test_delete():
    skill_id = 1
    response = client.delete("/skills/{skill_id}")

    assert response.status_code == 200, response.text
    data = response.json()

    response = client.get(f"/skills/{skill_id}")
    assert response.status_code == 404, None
