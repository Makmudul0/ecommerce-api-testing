# test_api.py
import requests

BASE_URL = 'http://localhost:5000'

def test_get_products():
    response = requests.get(f'{BASE_URL}/products')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_product():
    response = requests.get(f'{BASE_URL}/products/1')
    assert response.status_code == 200
    assert response.json()['id'] == 1

def test_add_product():
    new_product = {"name": "Tablet", "price": 300}
    response = requests.post(f'{BASE_URL}/products', json=new_product)
    assert response.status_code == 201
    assert response.json()['name'] == "Tablet"

def test_product_not_found():
    response = requests.get(f'{BASE_URL}/products/999')
    assert response.status_code == 404