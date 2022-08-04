import requests

import urllib.parse
from datetime import datetime


class Session(object):
    def __init__(self, base_url, token):
        self._base_url = base_url
        self._session = requests.Session()
        self._session.headers.update(Authorization='Bearer ' + token)

    def do(self, method, url, params=None, data=None, files=None):
        start_datetime = datetime.now()
        r = getattr(self._session, method)(urllib.parse.urljoin(self._base_url, url),
                                           params=params, data=data, files=files)
        print('{} {}: {} seconds'.format(method, url, (datetime.now() - start_datetime).total_seconds()))        
        r.raise_for_status()
        return r.json()
