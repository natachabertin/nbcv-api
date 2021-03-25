import pytest

from tests.db_utils import client
from tests.utils import get_the_first_id


def fill_db():
    """Not a test, use fixture to set up."""
    client.post("/users/", json={"username": "userA", "email": "userA@some.mail", "password": "pwdUserA"})
    client.post("/users/", json={"username": "userB", "email": "userB@some.mail", "password": "pwdUserB"})
    client.post("/users/", json={"username": "userC", "email": "userC@some.mail", "password": "pwdUserC"})
    client.post("/users/", json={"username": "userD", "email": "userD@some.mail", "password": "pwdUserD"})
    client.post("/users/", json={"username": "userE", "email": "userE@some.mail", "password": "pwdUserE"})
    client.post("/users/", json={"username": "userF", "email": "userF@some.mail", "password": "pwdUserF"})


def set_up():
    fill_db()


def test_create_all_required_data():
    response = client.post(
        "/users/",
        json={
            "username": "jdoe",
            "email": "jdoe@example.com",
            "password": "jDoe_pwd123"
        },
    )
    assert response.status_code == 201, response.text


def test_create_returns_all_but_pwd():
    response = client.post(
        "/users/",
        json={
            "username": "jdoe",
            "email": "jdoe@example.com",
            "password": "jDoe_pwd123"
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["username"] == "jdoe"
    assert data["email"] == "jdoe@example.com"
    assert "password" not in data


def test_create_missing_required_data():
    response = client.post(
        "/users/",
        json={
            "username": "jdoe",
            "password": "jDoe_pwd123"
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"][0]['msg'] == "field required"
    assert data["detail"][0]['type'] == "value_error.missing"
    assert data["detail"][0]['loc'] == ["body", "email"]


def test_create_email_is_validated_and_raise_error_if_wrong():
    response = client.post(
        "/users/",
        json={
            "username": "jdoe",
            "email": "email_wrong_format",
            "password": "jDoe_pwd123"
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"][0]['msg'] == "value is not a valid email address"
    assert data["detail"][0]['type'] == "value_error.email"
    assert data["detail"][0]['loc'] == ["body", "email"]


@pytest.mark.skip('Validate pwd secure and raise error')
def test_create_pwd_is_validated_and_raise_error_if_insecure():
    response = client.post(
        "/users/",
        json={
            "username": "jdoe",
            "email": "jdoe@example.com",
            "password": "insecurePassword"
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "Password must contain numbers, uppercase, lowercase and symbols"
    assert data["detail"]['type'] == "??"  # Check this one


def test_get_list_no_filters_returns_entire_list():
    set_up()
    response = client.get(f"/users/")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) > 5


def test_get_list_negative_skip_is_omitted():
    entire_list_len = len(client.get(f"/users/").json())
    skip = -5
    response = client.get(f"/users/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_negative_limit_is_omitted():
    entire_list_len = len(client.get(f"/users/").json())
    limit = -5
    response = client.get(f"/users/?limit={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_higher_than_list_limit_is_omitted():
    entire_list_len = len(client.get(f"/users/").json())
    limit = 3000
    response = client.get(f"/users/?limit={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_higher_than_list_skip_returns_empty():
    skip = 3000
    response = client.get(f"/users/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0


def test_get_list_filtered_with_skip_returns_shortened_list():
    entire_list_len = len(client.get(f"/users/").json())
    skip = 5
    response = client.get(f"/users/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len - skip


def test_get_list_filtered_with_limit_returns_shortened_list():
    entire_list_len = len(client.get(f"/users/").json())
    limit = 5
    response = client.get(f"/users/?skip={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len - limit


def test_get_list_filtered_skip_and_limit_same_number_returns_one_item():
    response = client.get(f"/users/?skip=1&limit=1")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 1


def test_get_list_filtered_skip_and_limit_zero_returns_empty():
    response = client.get(f"/users/?skip=0&limit=0")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0


def test_get_by_id_with_existing_id():
    user_id = get_the_first_id('users', client)
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == user_id
    assert "username" in data
    assert "email" in data
    assert "password" not in data


@pytest.mark.skip('Raise validation error on id not found.')
def test_get_by_id_with_non_existing_id():
    """Same behavior for zero and negatives."""
    user_id = 3000
    response = client.get(f"/users/{user_id}")

    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


@pytest.mark.skip("Auth data can't be updated just like that. Implement update feature when auth implementation.")
def test_update_auth_data_cant_be_done_like_other_entities():
    user_id = get_the_first_id('users', client)
    response = client.patch(
        f"/users/{user_id}",
        json={
            "username": "Another username",
            "email": "another@email.com",
            "password": "pwd_NEW123"
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "User data can't be updated all at once"
    assert data["detail"]['type'] == "??"


@pytest.mark.skip("Auth data can't be updated just like that. Implement update feature when auth implementation.")
def test_update_username_current_pwd_ok():
    user_id = get_the_first_id('users', client)
    response = client.patch(
        f"/users/{user_id}",
        json={
            "username": "anotherUsername",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["username"] == "anotherUsername"
    assert "email" in data
    assert "password" not in data


@pytest.mark.skip("Auth data can't be updated just like that. Implement update feature when auth implementation.")
def test_update_username_current_pwd_missing():
    user_id = get_the_first_id('users', client)
    response = client.patch(
        f"/users/{user_id}",
        json={
            "username": "anotherUsername",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["username"] == "anotherUsername"
    assert "email" in data
    assert "password" not in data


@pytest.mark.skip("Auth data can't be updated just like that. Implement update feature when auth implementation.")
def test_update_username_current_pwd_wrong():
    user_id = get_the_first_id('users', client)
    response = client.patch(
        f"/users/{user_id}",
        json={
            "username": "anotherUsername",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["username"] == "anotherUsername"
    assert "email" in data
    assert "password" not in data


@pytest.mark.skip("Auth data can't be updated just like that. Implement update feature when auth implementation.")
def test_update_username_new_value_invalid():
    user_id = get_the_first_id('users', client)
    response = client.patch(
        f"/users/{user_id}",
        json={
            "username": "anotherUsername",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["username"] == "anotherUsername"
    assert "email" in data
    assert "password" not in data


@pytest.mark.skip("Auth data can't be updated just like that. Implement update feature when auth implementation.")
def test_update_email_current_pwd_ok():
    user_id = get_the_first_id('users', client)
    response = client.patch(
        f"/users/{user_id}",
        json={
            "email": "another@email.com",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "another@email.com"
    assert "username" in data
    assert "password" not in data


@pytest.mark.skip("Auth data can't be updated just like that. Implement update feature when auth implementation.")
def test_update_email_current_pwd_missing():
    user_id = get_the_first_id('users', client)
    response = client.patch(
        f"/users/{user_id}",
        json={
            "email": "another@email.com",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "another@email.com"
    assert "username" in data
    assert "password" not in data


@pytest.mark.skip("Auth data can't be updated just like that. Implement update feature when auth implementation.")
def test_update_email_current_pwd_wrong():
    user_id = get_the_first_id('users', client)
    response = client.patch(
        f"/users/{user_id}",
        json={
            "email": "another@email.com",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "another@email.com"
    assert "username" in data
    assert "password" not in data


@pytest.mark.skip("Auth data can't be updated just like that. Implement update feature when auth implementation.")
def test_update_email_new_value_invalid():
    user_id = get_the_first_id('users', client)
    response = client.patch(
        f"/users/{user_id}",
        json={
            "email": "another@email.com",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "another@email.com"
    assert "username" in data
    assert "password" not in data


@pytest.mark.skip("Auth data can't be updated just like that. Implement update feature when auth implementation.")
def test_change_pwd_both_pwd_ok():
    user_id = get_the_first_id('users', client)
    response = client.patch(
        f"/users/{user_id}/change_password",
        json={
            "password": "securePWD123.",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "username" in data
    assert "email" in data
    assert "password" not in data


@pytest.mark.skip("Auth data can't be updated just like that. Implement update feature when auth implementation.")
def test_change_pwd_new_pwd_missing():
    user_id = get_the_first_id('users', client)
    response = client.patch(
        f"/users/{user_id}/change_password",
        json={
            "password": "securePWD123.",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "username" in data
    assert "email" in data
    assert "password" not in data


@pytest.mark.skip("Auth data can't be updated just like that. Implement update feature when auth implementation.")
def test_change_pwd_new_pwd_wrong():
    user_id = get_the_first_id('users', client)
    response = client.patch(
        f"/users/{user_id}/change_password",
        json={
            "password": "securePWD123.",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "username" in data
    assert "email" in data
    assert "password" not in data


@pytest.mark.skip("Auth data can't be updated just like that. Implement update feature when auth implementation.")
def test_change_pwd_old_pwd_missing():
    user_id = get_the_first_id('users', client)
    response = client.patch(
        f"/users/{user_id}/change_password",
        json={
            "password": "securePWD123.",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "username" in data
    assert "email" in data
    assert "password" not in data


@pytest.mark.skip("Auth data can't be updated just like that. Implement update feature when auth implementation.")
def test_change_pwd_old_pwd_wrong():
    user_id = get_the_first_id('users', client)
    response = client.patch(
        f"/users/{user_id}/change_password",
        json={
            "password": "securePWD123.",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "username" in data
    assert "email" in data
    assert "password" not in data


@pytest.mark.skip("Auth data can't be updated just like that. Implement update feature when auth implementation.")
def test_change_pwd_new_insecure_pwd():
    user_id = get_the_first_id('users', client)
    response = client.patch(
        f"/users/{user_id}/change_password",
        json={
            "password": "securePWD123.",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "username" in data
    assert "email" in data
    assert "password" not in data


def test_delete():
    user_id = get_the_first_id('users', client)
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 204, response.text


@pytest.mark.skip('Raise validation error on id not found.')
def test_delete_non_existing_id_raises_error():
    """Same behavior for zero and negatives."""
    user_id = 3000
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??"  # Check this one


@pytest.mark.skip('Raise validation error on id not found.')
def test_delete_non_existing_id_dont_delete_anything():
    """Same behavior for zero and negatives."""
    entire_list_len = len(client.get(f"/users/").json())
    user_id = entire_list_len + 10

    client.delete(f"/users/{user_id}")

    list_after_delete = len(client.get(f"/users/").json())

    assert list_after_delete == entire_list_len
