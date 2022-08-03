import pytest

from pathlib import Path

import rss


@pytest.fixture
def get_raw_mock(monkeypatch):
    with open((Path(__file__) / '..' / 'rss' / 'avtonom_full_rss').resolve(), 'r') as f:
        raw = f.read()
    monkeypatch.setattr(rss, 'get_raw', lambda: raw)
