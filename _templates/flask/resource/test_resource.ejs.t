---
to: tests/test_<%= name %>.py
---
import pytest


def test_root_page(test_client):
    """
    GIVEN a flask app
    WHEN the '/<%= name %>' page is requested
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert response.get_json() == { 'msg': '<%= name %>' }
