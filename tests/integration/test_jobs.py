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
    job_id = 1
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == job_id


def test_update():
    job_id = 1
    response = client.patch(
        f"/jobs/{job_id}",
        json={
            "title": "Another title",
            "company": "Another company",
            "achievements": "Another achievements"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "Another title"
    assert data["company"] == "Another company"
    assert data["achievements"] == "Another achievements"


@pytest.mark.skip(reason="Not implemented yet.")
def test_delete():
    job_id = 1
    response = client.delete("/jobs/{job_id}")

    assert response.status_code == 200, response.text
    data = response.json()

    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 404, None
