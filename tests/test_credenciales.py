import pytest


def test_root_page(test_client):
    """
    GIVEN a flask app
    WHEN the '/credenciales' page is requested
    """
    response = test_client.get('/credenciales')
    assert response.status_code == 200
    assert response.get_json() == { 'msg': 'credenciales' }
