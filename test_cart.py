import pytest

from .app import app


@pytest.fixture
def client():

    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_valid_cart(client):
    data = {
        'products': [
            {
                'product': 'milk',
                'price': 10,
                'quantity': 1
            },
            {
                'product': 'bread',
                'price': 6,
                'quantity': 2
            }
        ]
    }
    res = client.post('/api/v1/carts/cart/', json=data)
    assert res.status_code == 200
    assert res.json['total'] == 22


def test_empty_cart(client):
    data = {
        'products': []
    }
    res = client.post('/api/v1/carts/cart/', json=data)
    assert res.status_code == 400


def test_zero_quantiy_cart(client):
    data = {
        'products': [
            {
                'product': 'milk',
                'price': 10,
                'quantity': 0
            }
        ]
    }
    res = client.post('/api/v1/carts/cart/', json=data)
    assert res.status_code == 400
