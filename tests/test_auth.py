import pytest


def test_auth_login(test_client, init_db):
    """
    GIVEN a flask app
    WHEN the '/auth' page is requested
    """
    url = '{}/_login'.format(pytest.routes['users'])
    response = test_client.post(url, json={
        'email': 'test@test.com', 'password': 'test'
    })

    assert response.status_code == 200
    assert ('access_token' in response.get_json().keys()) == True

def test_token(test_client, init_db, token_access):
    url = '{}/_logout'.format(pytest.routes['users'])
    headers =  { 'Authorization' : 'Bearer {}'.format(token_access)}
    response = test_client.post(url,
                                headers=headers,
                                json={'email': 'test@test.com'})

    assert response.status_code == 200
    assert response.get_json() == {'msg': 'test@test.com logout'}

