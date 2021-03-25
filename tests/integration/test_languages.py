import pytest

from tests.db_utils import client
from tests.utils import get_the_first_id


def fill_db():
    """Not a test, use fixture to set up."""
    client.post("/languages/", json={"name": "A", "written_level": 8, "spoken_level": 6, "level_description": "advanced"})
    client.post("/languages/", json={"name": "B", "written_level": 8, "spoken_level": 6, "level_description": "advanced"})
    client.post("/languages/", json={"name": "C", "written_level": 8, "spoken_level": 6, "level_description": "advanced"})
    client.post("/languages/", json={"name": "D", "written_level": 8, "spoken_level": 6, "level_description": "advanced"})
    client.post("/languages/", json={"name": "E", "written_level": 8, "spoken_level": 6, "level_description": "advanced"})
    client.post("/languages/", json={"name": "F", "written_level": 8, "spoken_level": 6, "level_description": "advanced"})


def set_up():
    fill_db()


def test_create_all_required_data():
    response = client.post(
        "/languages/",
        json={
            "name": "Some name",
            "level_description": "Some level_description",
            "written_level": 8,
            "spoken_level": 5,
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["name"] == "Some name"
    assert data["level_description"] == "Some level_description"
    assert data["written_level"] == 8
    assert data["spoken_level"] == 5


@pytest.mark.skip('Make dates mandatory')
def test_create_missing_required_data():
    response = client.post(
        "/languages/",
        json={
            "name": "Some name",
            "level_description": "Some level_description",
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "field required"
    assert data["detail"]['type'] == "value_error.missing"


@pytest.mark.skip('Implement enums on categories')
def test_create_non_existing_category():
    response = client.post(
        "/languages/",
        json={
            "level_description": "not a level_description",
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "Level description doesn't exist"
    assert data["detail"]['type'] == "??"


@pytest.mark.skip('Validate int fields')
def test_create_level_is_validated_1_to_10():
    response = client.post(
        "/languages/",
        json={
            "written_level": 18,
            "spoken_level": 55,
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "Level must be a positive number between 1 and 10"
    assert data["detail"]['type'] == "??"


@pytest.mark.skip('Validate int fields')
def test_create_level_is_positive():
    response = client.post(
        "/languages/",
        json={
            "written_level": -8,
            "spoken_level": -5,
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "Level must be a positive number between 1 and 10"
    assert data["detail"]['type'] == "??"


def test_get_list_no_filters_returns_entire_list():
    set_up()
    response = client.get(f"/languages/")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) > 5


def test_get_list_negative_skip_is_omitted():
    entire_list_len = len(client.get(f"/languages/").json())
    skip = -5
    response = client.get(f"/languages/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_negative_limit_is_omitted():
    entire_list_len = len(client.get(f"/languages/").json())
    limit = -5
    response = client.get(f"/languages/?limit={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_higher_than_list_limit_is_omitted():
    entire_list_len = len(client.get(f"/languages/").json())
    limit = 3000
    response = client.get(f"/languages/?limit={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_higher_than_list_skip_returns_empty():
    skip = 3000
    response = client.get(f"/languages/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0


def test_get_list_filtered_with_skip_returns_shortened_list():
    entire_list_len = len(client.get(f"/languages/").json())
    skip = 5
    response = client.get(f"/languages/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len - skip


def test_get_list_filtered_with_limit_returns_shortened_list():
    entire_list_len = len(client.get(f"/languages/").json())
    limit = 5
    response = client.get(f"/languages/?skip={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len - limit


def test_get_list_filtered_skip_and_limit_same_number_returns_one_item():
    response = client.get(f"/languages/?skip=1&limit=1")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 1


def test_get_list_filtered_skip_and_limit_zero_returns_empty():
    response = client.get(f"/languages/?skip=0&limit=0")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0


def test_get_by_id_with_existing_id():
    language_id = get_the_first_id('languages', client)
    response = client.get(f"/languages/{language_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == language_id
    assert "name" in data
    assert "level_description" in data
    assert "written_level" in data
    assert "spoken_level" in data


@pytest.mark.skip('Raise validation error on id not found.')
def test_get_by_id_with_non_existing_id():
    """Same behavior for zero and negatives."""
    language_id = 3000
    response = client.get(f"/languages/{language_id}")

    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


def test_update_all_data():
    language_id = get_the_first_id('languages', client)
    response = client.patch(
        f"/languages/{language_id}",
        json={
            "name": "Another name",
            "level_description": "Another level_description",
            "written_level": 3,
            "spoken_level": 6,
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["level_description"] == "Another level_description"
    assert data["name"] == "Another name"
    assert data["written_level"] == 3
    assert data["spoken_level"] == 6


@pytest.mark.skip('Make Update fields optional')
def test_update_strings():
    language_id = get_the_first_id('language', client)
    response = client.patch(
        f"/languages/{language_id}",
        json={
            "name": "Update name",
            "level_description": "Update level_description",
            "status": "Update status"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["level_description"] == "Update level_description"
    assert data["name"] == "Update name"
    assert data["status"] == "Update status"
    assert data["written_level"] == 3
    assert data["spoken_level"] == 6


@pytest.mark.skip('Make Update fields optional')
def test_update_integers():
    language_id = get_the_first_id('language', client)
    response = client.patch(
        f"/languages/{language_id}",
        json={
            "written_level": 2,
            "spoken_level": 8,
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["level_description"] == "Update level_description"
    assert data["name"] == "Update name"
    assert data["status"] == "Update status"
    assert data["written_level"] == 2
    assert data["spoken_level"] == 8


@pytest.mark.skip('Raise validation error on id not found.')
def test_update_non_existing_id():
    """Same behavior for zero and negatives."""
    language_id = 3000
    response = client.patch(
        f"/languages/{language_id}",
        json={
            "name": "Another name",
            "level_description": "Another level_description",
            "written_level": 3,
            "spoken_level": 6,
            "status": "Another status"
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


def test_delete():
    language_id = get_the_first_id('language', client)
    response = client.delete(f"/languages/{language_id}")
    assert response.status_code == 204, response.text


@pytest.mark.skip('Raise validation error on id not found.')
def test_delete_non_existing_id_raises_error():
    """Same behavior for zero and negatives."""
    language_id = 3000
    response = client.delete(f"/languages/{language_id}")
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


@pytest.mark.skip('Raise validation error on id not found.')
def test_delete_non_existing_id_dont_delete_anything():
    """Same behavior for zero and negatives."""
    entire_list_len = len(client.get(f"/languages/").json())
    language_id = entire_list_len + 10

    client.delete(f"/languages/{language_id}")

    list_after_delete = len(client.get(f"/languages/").json())

    assert list_after_delete == entire_list_len
