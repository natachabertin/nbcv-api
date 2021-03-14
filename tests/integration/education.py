from tests.utils import client
import pytest

def test_create():
    response = client.post(
        "/education/",
        json={
            "school": "Some school",
            "degree": "Some degree",
            "status": "Completed"
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["school"] == "Some school"
    assert data["degree"] == "Some degree"
    assert data["status"] == "Completed"


def test_get_list():
    response = client.get(f"/education/")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_get_by_id():
    user_id = 1
    response = client.get(f"/education/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == user_id


@pytest.mark.skip(reason="Not implemented yet.")
def test_update():
    user_id = 1
    response = client.put(
        "/education/{user_id}",
        json={
            "school": "Another school"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["school"] == "Another school"

@pytest.mark.skip(reason="Not implemented yet.")
def test_delete():
    user_id = 1
    response = client.delete("/education/{user_id}")

    assert response.status_code == 200, response.text
    data = response.json()

    response = client.get(f"/education/{user_id}")
    assert response.status_code == 404, None
