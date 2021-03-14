from tests.utils import client
import pytest

def test_create():
    response = client.post(
        "/jobs/",
        json={
            "title": "title",
            "company": "company",
            "achievements": "achievements"
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["title"] == "title"
    assert data["company"] == "company"
    assert data["achievements"] == "achievements"


def test_get_list():
    response = client.get(f"/jobs/")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_get_by_id():
    user_id = 1
    response = client.get(f"/jobs/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == user_id


@pytest.mark.skip(reason="Not implemented yet.")
def test_update():
    user_id = 1
    response = client.put(
        "/jobs/{user_id}",
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
    response = client.delete("/jobs/{user_id}")

    assert response.status_code == 200, response.text
    data = response.json()

    response = client.get(f"/jobs/{user_id}")
    assert response.status_code == 404, None
