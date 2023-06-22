import pytest
from pydantic import BaseModel


class AccessToken(BaseModel):
    access_token: str


class User(BaseModel):
    id: int
    first_name: str
    last_name: str


def test_access_token_valid():
    request = {"access_token": "rtag341"}
    AccessToken(**request)


def test_access_token_hollow():
    request = {}
    with pytest.raises(ValueError):
        AccessToken(**request)


def test_access_token_false():
    request = {"access_token": "rteg143"}
    AccessToken(**request)


def test_users_get_response():
    response = [
        {"id": 74567917, "first_name": "Jack", "last_name": "Dowson"},
        {"id": 72157651, "first_name": "Kate", "last_name": "Austen"},
        {"id": 97657965, "first_name": "Charlie", "last_name": "Payce"},
    ]
    users = [User(**user) for user in response]


def test_users_get_true_response():
    response = [
        {"id": 74567917, "first_name": "Jack", "last_name": "Dowson"},
        {"id": 72157651, "first_name": "Kate", "last_name": "Austen"},
        {"id": 97657965, "first_name": "Charlie", "last_name": "Payce"},
    ]
    users = [User(**user) for user in response]
    assert len(users) == 3
    assert users[2].id == 97657965
    assert users[1].first_name == "Kate"
    assert users[0].last_name == "Dowson"
    assert users[0].first_name == "Jack"


def test_users_get_false_response():
    response = [{"false_key": "value"}]
    with pytest.raises(ValueError):
        users = [User(**user) for user in response]


def test_users_get_hollow():
    response = []
    users = [User(**user) for user in response]
    assert len(users) == 0


def test_user_false_id():
    user = {
        "id": "e#%3!p@09-",
        "first_name": "Charlie",
        "last_name": "Payce"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_user_clear_id():
    user = {
        "id": "",
        "first_name": "Charlie",
        "last_name": "Payce"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_user_fn_number_pass():
    user = {
        "id": 72157651,
        "first_name": 72157651,
        "last_name": "Austen"
    }
    User(**user)


def test_user_ln_number_pass():
    user = {
        "id": 72157651,
        "first_name": "Kate",
        "last_name": 72157651
    }
    User(**user)


def test_user_fn_clear_pass():
    user = {
        "id": 72157651,
        "first_name": "",
        "last_name": "Austen"
    }
    User(**user)


def test_user_ln_clear_pass():
    user = {
        "id": 74567917,
        "first_name": "Jack",
        "last_name": ""
    }
    User(**user)


def test_user_clear_info():
    user = {
        "id": "",
        "first_name": "",
        "last_name": ""
    }
    with pytest.raises(ValueError):
        User(**user)
