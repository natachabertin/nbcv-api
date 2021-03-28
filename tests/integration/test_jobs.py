import pytest

from tests.client import client
from tests.utils import get_the_first_id


def fill_db():
    """Not a test, use fixture to set up."""
    client.post("/jobs/", json={"title": "A", "company": "A", "achievements": "A", "start_date": "2016-03-02", "end_date": "2020-11-30"})
    client.post("/jobs/", json={"title": "B", "company": "B", "achievements": "B", "start_date": "2016-03-02", "end_date": "2020-11-30"})
    client.post("/jobs/", json={"title": "C", "company": "C", "achievements": "C", "start_date": "2016-03-02", "end_date": "2020-11-30"})
    client.post("/jobs/", json={"title": "D", "company": "D", "achievements": "D", "start_date": "2016-03-02", "end_date": "2020-11-30"})
    client.post("/jobs/", json={"title": "E", "company": "E", "achievements": "E", "start_date": "2016-03-02", "end_date": "2020-11-30"})
    client.post("/jobs/", json={"title": "F", "company": "F", "achievements": "F", "start_date": "2016-03-02", "end_date": "2020-11-30"})


def set_up():
    fill_db()


def test_create_all_required_data():
    response = client.post(
        "/jobs/",
        json={
            "title": "title",
            "company": "company",
            "start_date": "2016-03-02",
            "end_date": "2020-11-30",
            "achievements": "achievements"
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["title"] == "title"
    assert data["company"] == "company"
    assert data["achievements"] == "achievements"
    assert data["start_date"] == "2016-03-02"
    assert data["end_date"] == "2020-11-30"


def test_create_missing_required_data():
    response = client.post(
        "/jobs/",
        json={
            "title": "title",
            "company": "company",
            "achievements": "achievements"
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"][0]['msg'] == "field required"
    assert data["detail"][0]['type'] == "value_error.missing"
    assert data["detail"][0]['loc'] == ["body", 'start_date']
    assert data["detail"][1]['msg'] == "field required"
    assert data["detail"][1]['type'] == "value_error.missing"
    assert data["detail"][1]['loc'] == ["body", 'end_date']


def test_create_date_is_accepted_and_returned_as_string_date_formatted():
    response = client.post(
        "/jobs/",
        json={
            "title": "title",
            "company": "company",
            "start_date": "2016-03-02",
            "end_date": "2020-11-30",
            "achievements": "achievements"
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["start_date"] == "2016-03-02"
    assert data["end_date"] == "2020-11-30"


def test_get_list_no_filters_returns_entire_list():
    set_up()
    response = client.get(f"/jobs/")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) > 5


def test_get_list_negative_skip_is_omitted():
    entire_list_len = len(client.get(f"/jobs/").json())
    skip = -5
    response = client.get(f"/jobs/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_negative_limit_is_omitted():
    entire_list_len = len(client.get(f"/jobs/").json())
    limit = -5
    response = client.get(f"/jobs/?limit={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_higher_than_list_limit_is_omitted():
    entire_list_len = len(client.get(f"/jobs/").json())
    limit = 3000
    response = client.get(f"/jobs/?limit={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_higher_than_list_skip_returns_empty():
    skip = 3000
    response = client.get(f"/jobs/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0


def test_get_list_filtered_with_skip_returns_shortened_list():
    entire_list_len = len(client.get(f"/jobs/").json())
    skip = 5
    response = client.get(f"/jobs/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len - skip


def test_get_list_filtered_with_limit_returns_shortened_list():
    entire_list_len = len(client.get(f"/jobs/").json())
    limit = 5
    response = client.get(f"/jobs/?skip={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len - limit


def test_get_list_filtered_skip_and_limit_same_number_returns_one_item():
    response = client.get(f"/jobs/?skip=1&limit=1")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 1


def test_get_list_filtered_skip_and_limit_zero_returns_empty():
    response = client.get(f"/jobs/?skip=0&limit=0")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0


def test_get_by_id():
    job_id = get_the_first_id('jobs', client)
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == job_id


def test_get_by_id_with_existing_id():
    job_id = get_the_first_id('jobs', client)
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == job_id
    assert "title" in data
    assert "company" in data
    assert "achievements" in data
    assert "start_date" in data
    assert "end_date" in data


@pytest.mark.skip('Raise validation error on id not found.')
def test_get_by_id_with_non_existing_id():
    """Same behavior for zero and negatives."""
    job_id = 3000
    response = client.get(f"/jobs/{job_id}")

    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


def test_update_all_data():
    job_id = get_the_first_id('jobs', client)
    response = client.patch(
        f"/jobs/{job_id}",
        json={
            "title": "Another title",
            "company": "Another company",
            "start_date": "2011-03-02",
            "end_date": "2011-11-30",
            "achievements": "Another achievements"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["company"] == "Another company"
    assert data["title"] == "Another title"
    assert data["achievements"] == "Another achievements"
    assert data["start_date"] == "2011-03-02"
    assert data["end_date"] == "2011-11-30"


def test_update_strings():
    job_id = get_the_first_id('jobs', client)
    response = client.patch(
        f"/jobs/{job_id}",
        json={
            "title": "Update title",
            "company": "Update company",
            "achievements": "Update achievements"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["company"] == "Update company"
    assert data["title"] == "Update title"
    assert data["achievements"] == "Update achievements"
    assert data["start_date"] == "2011-03-02"
    assert data["end_date"] == "2011-11-30"


def test_update_dates():
    job_id = get_the_first_id('jobs', client)
    response = client.patch(
        f"/jobs/{job_id}",
        json={
            "start_date": "2000-01-01",
            "end_date": "2000-01-02",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["company"] == "Update company"
    assert data["title"] == "Update title"
    assert data["achievements"] == "Update achievements"
    assert data["start_date"] == "2000-01-01"
    assert data["end_date"] == "2000-01-02"


@pytest.mark.skip('Raise validation error on id not found.')
def test_update_non_existing_id():
    """Same behavior for zero and negatives."""
    job_id = 3000
    response = client.patch(
        f"/jobs/{job_id}",
        json={
            "title": "Another title",
            "company": "Another company",
            "start_date": "2011-03-02",
            "end_date": "2011-11-30",
            "achievements": "Another achievements"
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


def test_delete():
    job_id = get_the_first_id('jobs', client)
    response = client.delete(f"/jobs/{job_id}")
    assert response.status_code == 204, response.text


@pytest.mark.skip('Raise validation error on id not found.')
def test_delete_non_existing_id_raises_error():
    """Same behavior for zero and negatives."""
    job_id = 3000
    response = client.delete(f"/jobs/{job_id}")
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


@pytest.mark.skip('Raise validation error on id not found.')
def test_delete_non_existing_id_dont_delete_anything():
    """Same behavior for zero and negatives."""
    entire_list_len = len(client.get(f"/jobs/").json())
    job_id = entire_list_len + 10

    client.delete(f"/jobs/{job_id}")

    list_after_delete = len(client.get(f"/jobs/").json())

    assert list_after_delete == entire_list_len
