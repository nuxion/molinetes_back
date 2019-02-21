import pytest


@pytest.fixture(scope='module')
def token(test_client, init_db):
    endpoint = '{}/users'.format(pytest.url_prefix)
    url = '{}/login'.format(endpoint)
    response = test_client.post(url, json={
        'email': 'test@test.com', 'password': 'test'
    })
    token = response.json.get('access_token')

    yield token

def test_auth_login(test_client, init_db):
    """
    GIVEN a flask app
    WHEN the '/auth' page is requested
    """
    endpoint = '{}/users'.format(pytest.url_prefix)
    url = '{}/login'.format(endpoint)
    response = test_client.post(url, json={
        'email': 'test@test.com', 'password': 'test'
    })
    if 'access_token' in response.get_json().keys():
        exist = True
    else:
        exist = False

    assert response.status_code == 200
    assert exist == True

def test_token(test_client, init_db, token):
    endpoint = '{}/users'.format(pytest.url_prefix)
    url = '{}/login'.format(endpoint)
    headers =  { 'Authorization' : 'Bearer {}'.format(token) }
    response = test_client.get(url, headers=headers)

    assert response.status_code == 200
    assert response.get_json() == {"logged_in_as": "test@test.com"}

