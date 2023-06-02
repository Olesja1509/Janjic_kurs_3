from utils import utils
import pytest
import json

@pytest.fixture
def test_operations():
    with open('operations.json', encoding="utf-8") as file:
        return json.load(file)
def test_sorted_operations(test_operations):
    assert utils.sorted_operations() == [
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
        },
        {
            "id": 518707726,
            "state": "EXECUTED",
            "date": "2018-11-29T07:18:23.941293",
            "operationAmount": {
                "amount": "3348.98",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 3152479541115065",
            "to": "Visa Gold 9447344650495960"
        }]

def test_formatted_operations(test_operations):
    assert utils.formatted_operations(1) == [
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "08.12.2019",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет **5907"
        }]

    assert utils.formatted_operations(2) == [
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "08.12.2019",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет **5907"
        },
        {
            "id": 518707726,
            "state": "EXECUTED",
            "date": "29.11.2018",
            "operationAmount": {
                "amount": "3348.98",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 3152 47** **** 5065",
            "to": "Visa Gold 9447 34** **** 5960"
        }]
