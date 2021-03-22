from tests.db_utils import client
from tests.utils import get_the_first_id


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
    job_id = get_the_first_id('jobs', client)
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == job_id


def test_update():
    job_id = get_the_first_id('jobs', client)
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


def test_delete():
    job_id = get_the_first_id('jobs', client)
    response = client.delete(f"/jobs/{job_id}")
    assert response.status_code == 204, response.text
