import pytest
import requests_mock


from session import Session


@pytest.mark.parametrize('base_url', ('https://mastodon.example', 'https://mastodon.example/'))
def test_base_url(base_url):
    session = Session(base_url, 'XxxYyy')
    with requests_mock.mock() as mock:
        mock.get('https://mastodon.example/v1/endpoint', json={})
        session.do('get', 'v1/endpoint')

        assert mock.called


def test_token():
    session = Session('https://mastodon.example', 'XxxYyyZzzz')
    with requests_mock.mock() as mock:
        mock.post('https://mastodon.example/v1/endpoint', json={})
        session.do('post', 'v1/endpoint')

        assert mock.request_history[0].headers['Authorization'] == 'Bearer XxxYyyZzzz'
