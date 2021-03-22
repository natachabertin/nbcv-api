from tests.db_utils import client
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


def test_update():
    project_id = 1
    response = client.patch(
        f"/projects/{project_id}",
        json={
            "name": "Another Project",
            "description": "Another Project example"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Another Project"
    assert data["description"] == "Another Project example"


def test_delete():
    project_id = 1
    response = client.delete("/projects/{project_id}")
    assert response.status_code == 200, response.text

    response = client.get(f"/projects/{project_id}")
    assert response.status_code == 404, None
