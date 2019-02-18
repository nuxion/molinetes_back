import pytest


def test_root_page(test_client):
    """
    GIVEN a flask app
    WHEN the '/eventos' page is requested
    """
    response = test_client.get('/eventos')
    assert response.status_code == 200
    assert response.get_json() == { 'msg': 'eventos' }
