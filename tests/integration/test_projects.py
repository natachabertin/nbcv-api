from tests.utils import client
import pytest

def test_create():
    response = client.post(
        "/projects/",
        json={
            "name": "Project",
            "description": "Project example"
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["name"] == "Project"
    assert data["description"] == "Project example"


def test_get_list():
    response = client.get(f"/projects/")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_get_by_id():
    project_id = 1
    response = client.get(f"/projects/{project_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == project_id


@pytest.mark.skip(reason="Not implemented yet.")
def test_update():
    project_id = 1
    response = client.put(
        "/projects/{project_id}",
        json={
            "description": "another project description"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["description"] == "another project description"

@pytest.mark.skip(reason="Not implemented yet.")
def test_delete():
    project_id = 1
    response = client.delete("/projects/{project_id}")

    assert response.status_code == 200, response.text
    data = response.json()

    response = client.get(f"/projects/{project_id}")
    assert response.status_code == 404, None
