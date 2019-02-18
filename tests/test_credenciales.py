import pytest


def test_list_credenciales(test_client, init_db):
    """
    GIVEN a flask app
    WHEN the '/credenciales' page is requested
    """
    url = '{}/credenciales'.format(pytest.url_prefix)
    response = test_client.get(url)
    print("URLPREFIX: {}".format(pytest.url_prefix))
    assert response.status_code == 200
    assert len(response.get_json()) == 2

def test_post_credenciales(test_client, init_db):
    """
    GIVEN a flask app
    WHEN the '/credenciales' page is requested
    """
    url = '{}/credenciales'.format(pytest.url_prefix)
    response_post = test_client.post(url, json={'nombre':'test'})
    response_get = test_client.get(url)
    assert response_post.status_code == 201
    assert len(response_get.get_json()) == 3
