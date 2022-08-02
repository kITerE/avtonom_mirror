import pytest

from pathlib import Path


import avtonom_mirror


@pytest.fixture
def monkeypatch_get_raw(monkeypatch):
    with open((Path(__file__) / '..' / 'raw' / 'avtonom_full_rss').resolve(), 'rb') as f:
        raw = f.read()
    monkeypatch.setattr(avtonom_mirror, 'get_raw', lambda: raw)


def test_iterate_title(monkeypatch_get_raw):
    titles = [i.title for i in avtonom_mirror.iterate_items()]
    assert titles == [
        'Пока все не будут свободны: международная неделя солидарности с заключенными анархистами (23 — 30 августa 2022)',
        'АЧК-Бристоль: "R.I.P Тэйлор. Ярость – наше оружие"',
        'Александра Скочиленко останется в СИЗО до 1 сентября',
        'В Москве пройдет вечер поддержки антивоенных политзаключенных',
        'Способно ли человечество на самозащиту: «Тренды порядка и хаоса», эпизод 65 (31 июля)',
        'Беларусь: анархисты, осужденные по делу "Промня", год в заключении. Их новые адреса в колониях',
        'Дело о "дискредитации армии" против Евгения Каракашева прекращено за истечением срока давности',
        '"Канского подростка" Никиту Уварова этапировали в воспитательную колонию',
        'Самая интересная страна в мире: блиц-интервью с турецким анархистом',
        'Подельника Тесака приговорили к 16 годам по делу о "казни в лесу"',
        'Евгения Каракашева продолжат судить за «дискредитацию армии»',
        'Суд в Санкт-Петербурге рассмотрит продление ареста для Александры Скочиленко',
        'КиноКлуб в Клубе им. Джерри Рубина: "Что-то в воздухе"',
        'Порошок в шестерёнки системы: «Тренды порядка и хаоса», эпизод 64 (24 июля)',
        'Кириллу Украинцеву продлен арест',
        'Суд оставил Дмитрия Иванова в СИЗО до 2 сентября',
        'Роскомнадзор разблокировал сайт Tor Project',
        'Поддержка политзаключенных: вечер открыток в Москве и фестиваль в Санкт-Петербурге',
        'Петр Рябов: "Российские анархисты в 2000-2015 годах"',
        'Мосгорсуд оставил Дмитрия Иванова в СИЗО',
    ]
    print(next(avtonom_mirror.iterate_items()).image)
    assert False
