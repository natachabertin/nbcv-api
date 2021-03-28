import pytest

from tests.client import client
from tests.utils import get_the_first_id


def fill_db():
    """Not a test, use fixture to set up."""
    client.post("/trainings/", json={"school": "A", "title": "A", "certificate": "A", "end_date": "2020-11-30"})
    client.post("/trainings/", json={"school": "B", "title": "B", "certificate": "B", "end_date": "2020-11-30"})
    client.post("/trainings/", json={"school": "C", "title": "C", "certificate": "C", "end_date": "2020-11-30"})
    client.post("/trainings/", json={"school": "D", "title": "D", "certificate": "D", "end_date": "2020-11-30"})
    client.post("/trainings/", json={"school": "E", "title": "E", "certificate": "E", "end_date": "2020-11-30"})
    client.post("/trainings/", json={"school": "F", "title": "F", "certificate": "F", "end_date": "2020-11-30"})


def set_up():
    fill_db()


def test_create_all_required_data():
    response = client.post(
        "/trainings/",
        json={
            "school": "Some school",
            "title": "Some title",
            "end_date": "2020-11-30",
            "certificate": "Completed"
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["school"] == "Some school"
    assert data["title"] == "Some title"
    assert data["certificate"] == "Completed"
    assert data["end_date"] == "2020-11-30"


def test_create_missing_required_data():
    response = client.post(
        "/trainings/",
        json={
            "school": "Some school",
            "title": "Some title",
            "certificate": "Completed"
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"][0]['msg'] == "field required"
    assert data["detail"][0]['type'] == "value_error.missing"
    assert data["detail"][0]['loc'] == ["body", 'end_date']


def test_create_date_is_accepted_and_returned_as_string_date_formatted():
    response = client.post(
        "/trainings/",
        json={
            "school": "Some school",
            "title": "Some title",
            "end_date": "2020-11-30",
            "certificate": "Completed"
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["end_date"] == "2020-11-30"


def test_get_list_no_filters_returns_entire_list():
    set_up()
    response = client.get(f"/trainings/")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) > 5


def test_get_list_negative_skip_is_omitted():
    entire_list_len = len(client.get(f"/trainings/").json())
    skip = -5
    response = client.get(f"/trainings/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_negative_limit_is_omitted():
    entire_list_len = len(client.get(f"/trainings/").json())
    limit = -5
    response = client.get(f"/trainings/?limit={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_higher_than_list_limit_is_omitted():
    entire_list_len = len(client.get(f"/trainings/").json())
    limit = 3000
    response = client.get(f"/trainings/?limit={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_higher_than_list_skip_returns_empty():
    skip = 3000
    response = client.get(f"/trainings/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0


def test_get_list_filtered_with_skip_returns_shortened_list():
    entire_list_len = len(client.get(f"/trainings/").json())
    skip = 5
    response = client.get(f"/trainings/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len - skip


def test_get_list_filtered_with_limit_returns_shortened_list():
    entire_list_len = len(client.get(f"/trainings/").json())
    limit = 5
    response = client.get(f"/trainings/?skip={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len - limit


def test_get_list_filtered_skip_and_limit_same_number_returns_one_item():
    response = client.get(f"/trainings/?skip=1&limit=1")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 1


def test_get_list_filtered_skip_and_limit_zero_returns_empty():
    response = client.get(f"/trainings/?skip=0&limit=0")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0


def test_get_by_id_with_existing_id():
    training_id = get_the_first_id('trainings', client)
    response = client.get(f"/trainings/{training_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == training_id
    assert "school" in data
    assert "title" in data
    assert "certificate" in data
    assert "end_date" in data


@pytest.mark.skip('Raise validation error on id not found.')
def test_get_by_id_with_non_existing_id():
    """Same behavior for zero and negatives."""
    training_id = 3000
    response = client.get(f"/trainings/{training_id}")

    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


def test_update_all_data():
    training_id = get_the_first_id('trainings', client)
    response = client.patch(
        f"/trainings/{training_id}",
        json={
            "school": "Another school",
            "title": "Another title",
            "end_date": "2011-11-30",
            "certificate": "Another certificate"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "Another title"
    assert data["school"] == "Another school"
    assert data["certificate"] == "Another certificate"
    assert data["end_date"] == "2011-11-30"


def test_update_strings():
    training_id = get_the_first_id('trainings', client)
    response = client.patch(
        f"/trainings/{training_id}",
        json={
            "school": "Update school",
            "title": "Update title",
            "certificate": "Update certificate"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "Update title"
    assert data["school"] == "Update school"
    assert data["certificate"] == "Update certificate"
    assert data["end_date"] == "2011-11-30"


def test_update_dates():
    training_id = get_the_first_id('trainings', client)
    response = client.patch(
        f"/trainings/{training_id}",
        json={
            "end_date": "2000-01-02",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "Update title"
    assert data["school"] == "Update school"
    assert data["certificate"] == "Update certificate"
    assert data["end_date"] == "2000-01-02"


@pytest.mark.skip('Raise validation error on id not found.')
def test_update_non_existing_id():
    """Same behavior for zero and negatives."""
    training_id = 3000
    response = client.patch(
        f"/trainings/{training_id}",
        json={
            "school": "Another school",
            "title": "Another title",
            "end_date": "2011-11-30",
            "certificate": "Another certificate"
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


def test_delete():
    training_id = get_the_first_id('trainings', client)
    response = client.delete(f"/trainings/{training_id}")
    assert response.status_code == 204, response.text


@pytest.mark.skip('Raise validation error on id not found.')
def test_delete_non_existing_id_raises_error():
    """Same behavior for zero and negatives."""
    training_id = 3000
    response = client.delete(f"/trainings/{training_id}")
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


@pytest.mark.skip('Raise validation error on id not found.')
def test_delete_non_existing_id_dont_delete_anything():
    """Same behavior for zero and negatives."""
    entire_list_len = len(client.get(f"/trainings/").json())
    training_id = entire_list_len + 10

    client.delete(f"/trainings/{training_id}")

    list_after_delete = len(client.get(f"/trainings/").json())

    assert list_after_delete == entire_list_len
