import pytest

from tests.db_utils import client
from tests.utils import get_the_first_id


def fill_db():
    """Not a test, use fixture to set up."""
    client.post("/projects/", json={"name": "A", "description": "A", "start_date": "2016-03-02", "end_date": "2020-11-30"})
    client.post("/projects/", json={"name": "B", "description": "B", "start_date": "2016-03-02", "end_date": "2020-11-30"})
    client.post("/projects/", json={"name": "C", "description": "C", "start_date": "2016-03-02", "end_date": "2020-11-30"})
    client.post("/projects/", json={"name": "D", "description": "D", "start_date": "2016-03-02", "end_date": "2020-11-30"})
    client.post("/projects/", json={"name": "E", "description": "E", "start_date": "2016-03-02", "end_date": "2020-11-30"})
    client.post("/projects/", json={"name": "F", "description": "F", "start_date": "2016-03-02", "end_date": "2020-11-30"})


def set_up():
    fill_db()


def test_create_all_required_data():
    response = client.post(
        "/projects/",
        json={
            "name": "Some name",
            "description": "Some description",
            "start_date": "2016-03-02",
            "end_date": "2020-11-30"
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["name"] == "Some name"
    assert data["description"] == "Some description"
    assert data["start_date"] == "2016-03-02"
    assert data["end_date"] == "2020-11-30"


@pytest.mark.skip('Make dates mandatory')
def test_create_missing_required_data():
    response = client.post(
        "/projects/",
        json={
            "name": "Some name",
            "description": "Some description"
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "field required"
    assert data["detail"]['type'] == "value_error.missing"


def test_create_date_is_accepted_and_returned_as_string_date_formatted():
    response = client.post(
        "/projects/",
        json={
            "name": "Some name",
            "description": "Some description",
            "start_date": "2016-03-02",
            "end_date": "2020-11-30"
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["start_date"] == "2016-03-02"
    assert data["end_date"] == "2020-11-30"


def test_get_list_no_filters_returns_entire_list():
    set_up()
    response = client.get(f"/projects/")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) > 5


def test_get_list_negative_skip_is_omitted():
    entire_list_len = len(client.get(f"/projects/").json())
    skip = -5
    response = client.get(f"/projects/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_negative_limit_is_omitted():
    entire_list_len = len(client.get(f"/projects/").json())
    limit = -5
    response = client.get(f"/projects/?limit={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_higher_than_list_limit_is_omitted():
    entire_list_len = len(client.get(f"/projects/").json())
    limit = 3000
    response = client.get(f"/projects/?limit={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_higher_than_list_skip_returns_empty():
    skip = 3000
    response = client.get(f"/projects/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0


def test_get_list_filtered_with_skip_returns_shortened_list():
    entire_list_len = len(client.get(f"/projects/").json())
    skip = 5
    response = client.get(f"/projects/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len - skip


def test_get_list_filtered_with_limit_returns_shortened_list():
    entire_list_len = len(client.get(f"/projects/").json())
    limit = 5
    response = client.get(f"/projects/?skip={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len - limit


def test_get_list_filtered_skip_and_limit_same_number_returns_one_item():
    response = client.get(f"/projects/?skip=1&limit=1")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 1


def test_get_list_filtered_skip_and_limit_zero_returns_empty():
    response = client.get(f"/projects/?skip=0&limit=0")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0


def test_get_by_id_with_existing_id():
    project_id = get_the_first_id('projects', client)
    response = client.get(f"/projects/{project_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == project_id
    assert "name" in data
    assert "description" in data
    assert "start_date" in data
    assert "end_date" in data


@pytest.mark.skip('Raise validation error on id not found.')
def test_get_by_id_with_non_existing_id():
    """Same behavior for zero and negatives."""
    project_id = 3000
    response = client.get(f"/projects/{project_id}")

    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


def test_update_all_data():
    project_id = get_the_first_id('projects', client)
    response = client.patch(
        f"/projects/{project_id}",
        json={
            "name": "Another name",
            "description": "Another description",
            "start_date": "2011-03-02",
            "end_date": "2011-11-30",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["description"] == "Another description"
    assert data["name"] == "Another name"
    assert data["start_date"] == "2011-03-02"
    assert data["end_date"] == "2011-11-30"


@pytest.mark.skip('Make Update fields optional')
def test_update_strings():
    project_id = get_the_first_id('projects', client)
    response = client.patch(
        f"/projects/{project_id}",
        json={
            "name": "Update name",
            "description": "Update description",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["description"] == "Update description"
    assert data["name"] == "Update name"
    assert data["start_date"] == "2011-03-02"
    assert data["end_date"] == "2011-11-30"


@pytest.mark.skip('Make Update fields optional')
def test_update_dates():
    project_id = get_the_first_id('projects', client)
    response = client.patch(
        f"/projects/{project_id}",
        json={
            "start_date": "2000-01-01",
            "end_date": "2000-01-02",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["description"] == "Update description"
    assert data["name"] == "Update name"
    assert data["start_date"] == "2000-01-01"
    assert data["end_date"] == "2000-01-02"


@pytest.mark.skip('Raise validation error on id not found.')
def test_update_non_existing_id():
    """Same behavior for zero and negatives."""
    project_id = 3000
    response = client.patch(
        f"/projects/{project_id}",
        json={
            "name": "Another name",
            "description": "Another description",
            "start_date": "2011-03-02",
            "end_date": "2011-11-30",
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


def test_delete():
    project_id = get_the_first_id('projects', client)
    response = client.delete(f"/projects/{project_id}")
    assert response.status_code == 204, response.text


@pytest.mark.skip('Raise validation error on id not found.')
def test_delete_non_existing_id_raises_error():
    """Same behavior for zero and negatives."""
    project_id = 3000
    response = client.delete(f"/projects/{project_id}")
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


@pytest.mark.skip('Raise validation error on id not found.')
def test_delete_non_existing_id_dont_delete_anything():
    """Same behavior for zero and negatives."""
    entire_list_len = len(client.get(f"/projects/").json())
    project_id = entire_list_len + 10

    client.delete(f"/projects/{project_id}")

    list_after_delete = len(client.get(f"/projects/").json())

    assert list_after_delete == entire_list_len

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
    project_id = get_the_first_id('projects', client)
    response = client.get(f"/projects/{project_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == project_id


def test_update():
    project_id = get_the_first_id('projects', client)
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
    project_id = get_the_first_id('projects', client)
    response = client.delete(f"/projects/{project_id}")
    assert response.status_code == 204, response.text
