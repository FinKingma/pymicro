import pytest
import os
import json
from app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_products(client):
    response = client.get('/products')
    assert 200 == response.status_code
    assert 'Essence' == json.loads(response.data)['data'][0]['brand']