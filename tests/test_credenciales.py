import pytest


def test_list_credenciales(test_client, init_db):
    """
    GIVEN a flask app
    WHEN the '/credenciales' page is requested
    """
    response = test_client.get('/credenciales')
    assert response.status_code == 200
    assert len(response.get_json()) == 2

def test_post_credenciales(test_client, init_db):
    """
    GIVEN a flask app
    WHEN the '/credenciales' page is requested
    """
    response_post = test_client.post('/credenciales', json={'nombre':'test'})
    response_get = test_client.get('/credenciales')
    assert response_post.status_code == 201
    assert len(response_get.get_json()) == 3
