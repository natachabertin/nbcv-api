from tests.db_utils import client
from tests.utils import get_the_first_id


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
    language_id = get_the_first_id('languages', client)
    response = client.get(f"/languages/{language_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == language_id


def test_update():
    language_id = get_the_first_id('languages', client)
    response = client.patch(
        f"/languages/{language_id}",
        json={
            "name": "Another French",
            "level_description": "Another Intermediate",
            "written_level": 7,
            "spoken_level": 4
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Another French"
    assert data["level_description"] == "Another Intermediate"
    assert data["written_level"] == 7
    assert data["spoken_level"] == 4


def test_delete():
    language_id = get_the_first_id('languages', client)
    response = client.delete(f"/languages/{language_id}")
    assert response.status_code == 204, response.text
