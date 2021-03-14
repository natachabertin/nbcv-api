from tests.utils import client
import pytest

def test_create():
    response = client.post(
        "/languages/",
        json={
            "name": "French",
            "level_description": "Intermediate",
            "written_level": 8,
            "spoken_level": 5
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["name"] == "French"
    assert data["level_description"] == "Intermediate"
    assert data["written_level"] == 8
    assert data["spoken_level"] == 5


def test_get_list():
    response = client.get(f"/languages/")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_get_by_id():
    language_id = 1
    response = client.get(f"/languages/{language_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == language_id


@pytest.mark.skip(reason="Not implemented yet.")
def test_update():
    language_id = 1
    response = client.put(
        "/languages/{language_id}",
        json={
            "level_description": "Advanced"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["level_description"] == "Advanced"

@pytest.mark.skip(reason="Not implemented yet.")
def test_delete():
    language_id = 1
    response = client.delete("/languages/{language_id}")

    assert response.status_code == 200, response.text
    data = response.json()

    response = client.get(f"/languages/{language_id}")
    assert response.status_code == 404, None