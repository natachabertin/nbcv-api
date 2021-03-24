import pytest

from tests.db_utils import client
from tests.utils import get_the_first_id

def fill_db():
    """Not a test, use fixture to set up."""
    client.post("/education/", json={ "school": "A", "degree": "A", "status": "Completed", "start_date": "2016-03-02T18:38:53.654Z", "end_date": "2020-11-30T18:38:53.654Z"})
    client.post("/education/", json={ "school": "B", "degree": "B", "status": "Completed", "start_date": "2016-03-02T18:38:53.654Z", "end_date": "2020-11-30T18:38:53.654Z"})
    client.post("/education/", json={ "school": "C", "degree": "C", "status": "Completed", "start_date": "2016-03-02T18:38:53.654Z", "end_date": "2020-11-30T18:38:53.654Z"})
    client.post("/education/", json={ "school": "D", "degree": "D", "status": "Completed", "start_date": "2016-03-02T18:38:53.654Z", "end_date": "2020-11-30T18:38:53.654Z"})
    client.post("/education/", json={ "school": "E", "degree": "E", "status": "Completed", "start_date": "2016-03-02T18:38:53.654Z", "end_date": "2020-11-30T18:38:53.654Z"})
    client.post("/education/", json={ "school": "F", "degree": "F", "status": "Completed", "start_date": "2016-03-02T18:38:53.654Z", "end_date": "2020-11-30T18:38:53.654Z"})

def set_up():
    fill_db()


def test_create_all_required_data():
    response = client.post(
        "/education/",
        json={
            "school": "Some school",
            "degree": "Some degree",
            "start_date": "2016-03-02T18:38:53.654Z",
            "end_date": "2020-11-30T18:38:53.654Z",
            "status": "Completed"
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["school"] == "Some school"
    assert data["degree"] == "Some degree"
    assert data["status"] == "Completed"
    assert data["start_date"] == "2016-03-02T18:38:53.654000"
    assert data["end_date"] == "2020-11-30T18:38:53.654000"


@pytest.mark.skip('Make dates mandatory')
def test_create_missing_required_data():
    response = client.post(
        "/education/",
        json={
            "school": "Some school",
            "degree": "Some degree",
            "status": "Completed"
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "field required"
    assert data["detail"]['type'] == "value_error.missing"


def test_create_date_is_accepted_and_returned_as_string_dateformatted():
    response = client.post(
        "/education/",
        json={
            "school": "Some school",
            "degree": "Some degree",
            "start_date": "2016-03-02T18:38:53.654Z",
            "end_date": "2020-11-30T18:38:53.654Z",
            "status": "Completed"
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["start_date"] == "2016-03-02T18:38:53.654000"
    assert data["end_date"] == "2020-11-30T18:38:53.654000"


def test_get_list_no_filters_returns_entire_list():
    set_up()
    response = client.get(f"/education/")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) > 5


def test_get_list_negative_skip_is_omitted():
    entire_list_len = len(client.get(f"/education/").json())
    skip = -5
    response = client.get(f"/education/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_negative_limit_is_omitted():
    entire_list_len = len(client.get(f"/education/").json())
    limit = -5
    response = client.get(f"/education/?limit={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_higher_than_list_limit_is_omitted():
    entire_list_len = len(client.get(f"/education/").json())
    limit = 3000
    response = client.get(f"/education/?limit={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len


def test_get_list_higher_than_list_skip_returns_empty():
    entire_list_len = len(client.get(f"/education/").json())
    skip = 3000
    response = client.get(f"/education/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0


def test_get_list_filtered_with_skip_returns_shortened_list():
    entire_list_len = len(client.get(f"/education/").json())
    skip = 5
    response = client.get(f"/education/?skip={skip}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len - skip


def test_get_list_filtered_with_limit_returns_shortened_list():
    entire_list_len = len(client.get(f"/education/").json())
    limit = 5
    response = client.get(f"/education/?skip={limit}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == entire_list_len - limit


def test_get_list_filtered_skip_and_limit_same_number_returns_one_item():
    response = client.get(f"/education/?skip=1&limit=1")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 1


def test_get_list_filtered_skip_and_limit_zero_returns_empty():
    response = client.get(f"/education/?skip=0&limit=0")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0


@pytest.mark.skip('Make dates mandatory')
def test_get_by_id_with_existing_id():
    education_id = get_the_first_id('education', client)
    response = client.get(f"/education/{education_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == education_id
    assert data["school"] == "Some school"
    assert data["degree"] == "Some degree"
    assert data["status"] == "Completed"
    assert data["start_date"] == "2016-03-02T18:38:53.654000"
    assert data["end_date"] == "2020-11-30T18:38:53.654000"


@pytest.mark.skip('Raise validation error on id not found.')
def test_get_by_id_with_non_existing_id():
    """Same behavior for zero and negatives."""
    education_id = 3000
    response = client.get(f"/education/{education_id}")

    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??" # Check this one


def test_update_all_data():
    education_id = get_the_first_id('education', client)
    response = client.patch(
        f"/education/{education_id}",
        json={
            "school": "Another school",
            "degree": "Another degree",
            "start_date": "2011-03-02T18:38:53.654Z",
            "end_date": "2011-11-30T18:38:53.654Z",
            "status": "Another status"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["degree"] == "Another degree"
    assert data["school"] == "Another school"
    assert data["status"] == "Another status"
    assert data["start_date"] == "2011-03-02T18:38:53.654000"
    assert data["end_date"] == "2011-11-30T18:38:53.654000"


@pytest.mark.skip('Make Update fields optional')
def test_update_strings():
    education_id = get_the_first_id('education', client)
    response = client.patch(
        f"/education/{education_id}",
        json={
            "school": "Update school",
            "degree": "Update degree",
            "status": "Update status"
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["degree"] == "Update degree"
    assert data["school"] == "Update school"
    assert data["status"] == "Update status"
    assert data["start_date"] == "2011-03-02T18:38:53.654000"
    assert data["end_date"] == "2011-11-30T18:38:53.654000"


@pytest.mark.skip('Make Update fields optional')
def test_update_dates():
    education_id = get_the_first_id('education', client)
    response = client.patch(
        f"/education/{education_id}",
        json={
            "start_date": "2000-01-01T18:38:53.654Z",
            "end_date": "2000-01-02T18:38:53.654Z",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["degree"] == "Update degree"
    assert data["school"] == "Update school"
    assert data["status"] == "Update status"
    assert data["start_date"] == "2000-01-01T18:38:53.654000"
    assert data["end_date"] == "2000-01-02T18:38:53.654000"


@pytest.mark.skip('Raise validation error on id not found.')
def test_update_non_existing_id():
    """Same behavior for zero and negatives."""
    education_id = 3000
    response = client.patch(
        f"/education/{education_id}",
        json={
            "school": "Another school",
            "degree": "Another degree",
            "start_date": "2011-03-02T18:38:53.654Z",
            "end_date": "2011-11-30T18:38:53.654Z",
            "status": "Another status"
        },
    )
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??" # Check this one


def test_delete():
    education_id = get_the_first_id('education', client)
    response = client.delete(f"/education/{education_id}")
    assert response.status_code == 204, response.text


@pytest.mark.skip('Raise validation error on id not found.')
def test_delete_non_existing_id_raises_error():
    """Same behavior for zero and negatives."""
    education_id = 3000
    response = client.delete(f"/education/{education_id}")
    assert response.status_code == 422, response.text
    data = response.json()
    assert data["detail"]['msg'] == "ID not found"
    assert data["detail"]['type'] == "??" # Check this one


@pytest.mark.skip('Raise validation error on id not found.')
def test_delete_non_existing_id_dont_delete_anything():
    """Same behavior for zero and negatives."""
    entire_list_len = len(client.get(f"/education/").json())
    education_id = entire_list_len + 10

    client.delete(f"/education/{education_id}")

    list_after_delete = len(client.get(f"/education/").json())

    assert list_after_delete == entire_list_len
