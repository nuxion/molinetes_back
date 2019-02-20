import pytest


def test_auth_login(test_client, init_db):
    """
    GIVEN a flask app
    WHEN the '/auth' page is requested
    """
    url = '{}/actions/login'.format(pytest.url_prefix)
    response = test_client.post(url, json={
        'email': 'test@test.com', 'password': 'test'
    })
    if 'access_token' in response.get_json().keys():
        exist = True
    else:
        exist = False

    assert response.status_code == 200
    assert exist == True
