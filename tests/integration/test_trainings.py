import pytest

from tests.utils import client


def test_create():
    response = client.post(
        "/trainings/",
        json={
            "title": "jdoe",
            "school": "school",
            "end_date": "2021-03-14T15:36:29.896Z"
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["title"] == "jdoe"
    assert data["school"] == "school"
    assert data["end_date"] == "2021-03-14T15:36:29.896000"


def test_get_list():
    response = client.get(f"/trainings/")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_get_by_id():
    training_id = 1
    response = client.get(f"/trainings/{training_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == training_id


def test_update():
    training_id = 1
    response = client.patch(
        f"/trainings/{training_id}",
        json={
            "title": "title",
            "school": "other school",
            "end_date": "2021-10-14T15:36:29.896Z"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "title"
    assert data["school"] == "other school"
    assert data["end_date"] == "2021-10-14T15:36:29.896000"


@pytest.mark.skip(reason="Not implemented yet.")
def test_delete():
    training_id = 1

    response = client.delete(f"/trainings/{training_id}")
    assert response.status_code == 200, response.text

    response = client.get(f"/trainings/{training_id}")
    assert response.status_code == 404, None
