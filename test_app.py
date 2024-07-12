import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_valid_order(client):
    response = client.post('/api/orders', json={
        "name": "Melody Holiday Inn",
        "price": 2000,  
        "currency": "TWD"
    })
    assert response.status_code == 200

def test_invalid_name_characters(client):
    response = client.post('/api/orders', json={
        "name": "Melody Holiday 旅館",
        "price": 1500,
        "currency": "TWD"
    })
    assert response.status_code == 400
    assert '400 - name contains non-english characters' in response.json['errors']

def test_invalid_name_capitalization(client):
    response = client.post('/api/orders', json={
        "name": "melody Holiday Inn",
        "price": 1500,
        "currency": "TWD"
    })
    assert response.status_code == 400
    assert '400 - name is not capitalized' in response.json['errors']

def test_price_over_2000(client):
    response = client.post('/api/orders', json={
        "name": "Melody Holiday Inn",
        "price": 2051,
        "currency": "TWD"
    })
    assert response.status_code == 400
    assert '400 - price is over 2000' in response.json['errors']

def test_invalid_currency_format(client):
    response = client.post('/api/orders', json={
        "name": "Melody Holiday Inn",
        "price": 1500,
        "currency": "JPY"
    })
    assert response.status_code == 400
    assert '400 - currency format is wrong' in response.json['errors']

def test_convert_usd_to_twd(client):
    response = client.post('/api/orders', json={
        "name": "Melody Holiday Inn",
        "price": 20,  # 美元金額
        "currency": "USD"
    })
    assert response.status_code == 200
    assert response.json['currency'] == 'TWD'
    assert response.json['price'] == 620.0  # 20 USD 轉換為 TWD 應為 620 元

def test_convert_usd_to_twd_over2000(client):
    response = client.post('/api/orders', json={
        "name": "Melody Holiday Inn",
        "price": 100,  # 超過 2000 台幣金額
        "currency": "USD"
    })
    assert response.status_code == 400
    assert '400 - price is over 2000' in response.json['errors']

