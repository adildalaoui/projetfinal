import pytest
from app import app, db, Product

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_add_product(client):
    response = client.post('/api/products', json={'name': 'Test Product', 'quantity': 10})
    assert response.status_code == 201
    assert response.json['id'] is not None

def test_get_products(client):
    client.post('/api/products', json={'name': 'Test Product', 'quantity': 10})
    response = client.get('/api/products')
    assert response.status_code == 200
    assert len(response.json) > 0

def test_update_product(client):
    response = client.post('/api/products', json={'name': 'Test Product', 'quantity': 10})
    product_id = response.json['id']
    response = client.put(f'/api/products/{product_id}', json={'quantity': 20})
    assert response.status_code == 200
    assert response.json['quantity'] == 20

def test_delete_product(client):
    response = client.post('/api/products', json={'name': 'Test Product', 'quantity': 10})
    product_id = response.json['id']
    response = client.delete(f'/api/products/{product_id}')
    assert response.status_code == 204
    response = client.get('/api/products')
    assert not any(p['id'] == product_id for p in response.json)



