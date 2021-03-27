import pytest

from tests.test_client import client
from tests.utils import get_the_first_id


def fill_db():
    """Not a test, use fixture to set up."""
    client.post("/skills/", json={"name": "A", "level": 8, "category": "front-end"})
    client.post("/skills/", json={"name": "B", "level": 8, "category": "front-end"})
    client.post("/skills/", json={"name": "C", "level": 8, "category": "front-end"})
    client.post("/skills/", json={"name": "D", "level": 8, "category": "front-end"})
    client.post("/skills/", json={"name": "E", "level": 8, "category": "front-end"})
    client.post("/skills/", json={"name": "F", "level": 8, "category": "front-end"})


def set_up():
    fill_db()


def test_create_all_required_data():
    response = client.post(
        "/skills/",
        json={
            "name": "Some name",
            "category": "databases",
            "level": 6
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["name"] == "Some name"
    assert data["category"] == "databases"
    assert data["level"] == 6


def test_create_missing_required_data():
    response = client.post(
        "/skills/",
        json={
            "category": "databases",
            "level": 6
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"][0]['msg'] == "field required"
    assert data["detail"][0]['type'] == "value_error.missing"
    assert data["detail"][0]['loc'] == ["body", 'name']


@pytest.mark.skip('Implement categ as enums.')
def test_create_non_existing_category():
    response = client.post(
        "/skills/",
        json={
            "category": "not a category",
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "Category doesn't exist"
    assert data["detail"]['type'] == "value_error.missing"


@pytest.mark.skip('Implement integer validations.')
def test_create_level_is_validated_1_to_10():
    response = client.post(
        "/skills/",
        json={
            "level": 11
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "Level must be a positive number between 1 and 10"
    assert data["detail"]['type'] == "??"


@pytest.mark.skip('Implement integer validations.')
def test_create_level_is_positive():
    response = client.post(
        "/skills/",
        json={
            "level": -5
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "Level must be a positive number between 1 and 10"
    assert data["detail"]['type'] == "??"


def test_get_list_no_filters_returns_entire_list():
    set_up()
    response = client.get(f"/skills/")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) > 5


def test_get_list_negative_skip_is_omitted():
    entire_list_len = len(client.get(f"/skills/").json())
    skip = -5
    response = client.get(f"/skills/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_negative_limit_is_omitted():
    entire_list_len = len(client.get(f"/skills/").json())
    limit = -5
    response = client.get(f"/skills/?limit={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_higher_than_list_limit_is_omitted():
    entire_list_len = len(client.get(f"/skills/").json())
    limit = 3000
    response = client.get(f"/skills/?limit={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_higher_than_list_skip_returns_empty():
    skip = 3000
    response = client.get(f"/skills/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0


def test_get_list_filtered_with_skip_returns_shortened_list():
    entire_list_len = len(client.get(f"/skills/").json())
    skip = 5
    response = client.get(f"/skills/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len - skip


def test_get_list_filtered_with_limit_returns_shortened_list():
    entire_list_len = len(client.get(f"/skills/").json())
    limit = 5
    response = client.get(f"/skills/?skip={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len - limit


def test_get_list_filtered_skip_and_limit_same_number_returns_one_item():
    response = client.get(f"/skills/?skip=1&limit=1")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 1


def test_get_list_filtered_skip_and_limit_zero_returns_empty():
    response = client.get(f"/skills/?skip=0&limit=0")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0


def test_get_by_id_with_existing_id():
    skill_id = get_the_first_id('skills', client)
    response = client.get(f"/skills/{skill_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == skill_id
    assert "name" in data
    assert "category" in data
    assert "level" in data


@pytest.mark.skip('Raise validation error on id not found.')
def test_get_by_id_with_non_existing_id():
    """Same behavior for zero and negatives."""
    skill_id = 3000
    response = client.get(f"/skills/{skill_id}")

    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


def test_update_all_data():
    skill_id = get_the_first_id('skills', client)
    response = client.patch(
        f"/skills/{skill_id}",
        json={
            "name": "Another name",
            "category": "Another category",
            "level": 9
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["category"] == "Another category"
    assert data["name"] == "Another name"
    assert data["level"] == 9


def test_update_strings():
    skill_id = get_the_first_id('skills', client)
    response = client.patch(
        f"/skills/{skill_id}",
        json={
            "name": "Update name",
            "category": "Update category",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["category"] == "Update category"
    assert data["name"] == "Update name"
    assert data["level"] == 9


def test_update_dates():
    skill_id = get_the_first_id('skills', client)
    response = client.patch(
        f"/skills/{skill_id}",
        json={
            "level": 3
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["category"] == "Update category"
    assert data["name"] == "Update name"
    assert data["level"] == 3


@pytest.mark.skip('Raise validation error on id not found.')
def test_update_non_existing_id():
    """Same behavior for zero and negatives."""
    skill_id = 3000
    response = client.patch(
        f"/skills/{skill_id}",
        json={
            "name": "Another name",
            "category": "Another category",
            "level": "Another status"
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


def test_delete():
    skill_id = get_the_first_id('skills', client)
    response = client.delete(f"/skills/{skill_id}")
    assert response.status_code == 204, response.text


@pytest.mark.skip('Raise validation error on id not found.')
def test_delete_non_existing_id_raises_error():
    """Same behavior for zero and negatives."""
    skill_id = 3000
    response = client.delete(f"/skills/{skill_id}")
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


@pytest.mark.skip('Raise validation error on id not found.')
def test_delete_non_existing_id_dont_delete_anything():
    """Same behavior for zero and negatives."""
    entire_list_len = len(client.get(f"/skills/").json())
    skill_id = entire_list_len + 10

    client.delete(f"/skills/{skill_id}")

    list_after_delete = len(client.get(f"/skills/").json())

    assert list_after_delete == entire_list_len
