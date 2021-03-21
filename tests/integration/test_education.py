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
    education_id = 1
    response = client.get(f"/education/{education_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == education_id


def test_update():
    education_id = 1
    response = client.patch(
        f"/education/{education_id}",
        json={
            "school": "Another school",
            "degree": "Another degree",
            "status": "Another status"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["degree"] == "Another degree"
    assert data["school"] == "Another school"
    assert data["status"] == "Another status"


@pytest.mark.skip(reason="Not implemented yet.")
def test_delete():
    education_id = 1
    response = client.delete(f"/education/{education_id}")

    assert response.status_code == 200, response.text
    data = response.json()

    response = client.get(f"/education/{education_id}")
    assert response.status_code == 404, None
