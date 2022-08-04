import rss


def test_iterate_title(get_raw_mock):
    titles = [i.title for i in rss.iterate_items()]
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


def test_iterate_link(get_raw_mock):
    links = [i.link for i in rss.iterate_items()]
    assert links == [
        'https://avtonom.org/news/poka-vse-ne-budut-svobodny-mezhdunarodnaya-nedelya-solidarnosti-s-zaklyuchennymi-anarhistami-23',
        'https://avtonom.org/freenews/achk-bristol-rip-teylor-yarost-nashe-oruzhie',
        'https://avtonom.org/news/aleksandra-skochilenko-ostanetsya-v-sizo-do-1-sentyabrya',
        'https://avtonom.org/news/v-moskve-proydet-vecher-podderzhki-antivoennyh-politzaklyuchennyh',
        'https://avtonom.org/news/sposobno-li-chelovechestvo-na-samozashchitu-trendy-poryadka-i-haosa-epizod-65-31-iyulya',
        'https://avtonom.org/blog/belarus-anarhisty-osuzhdennye-po-delu-promnya-god-v-zaklyuchenii',
        'https://avtonom.org/news/delo-o-diskreditacii-armii-protiv-evgeniya-karakasheva-prekrashcheno-za-istecheniem-sroka',
        'https://avtonom.org/news/kanskogo-podrostka-nikitu-uvarova-etapirovali-v-vospitatelnuyu-koloniyu',
        'https://avtonom.org/pages/samaya-interesnaya-strana-v-mire-blic-intervyu-s-tureckim-anarhistom',
        'https://avtonom.org/news/podelnika-tesaka-prigovorili-k-16-godam-po-delu-o-kazni-v-lesu-1',
        'https://avtonom.org/news/evgeniya-karakasheva-prodolzhat-sudit-za-diskreditaciyu-armii',
        'https://avtonom.org/news/sud-v-sankt-peterburge-rassmotrit-prodlenie-aresta-dlya-aleksandry-skochilenko',
        'https://avtonom.org/news/kinoklub-v-klube-im-dzherri-rubina-chto-v-vozduhe',
        'https://avtonom.org/news/poroshok-v-shestyorenki-sistemy-trendy-poryadka-i-haosa-epizod-64-24-iyulya',
        'https://avtonom.org/news/kirillu-ukraincevu-prodlen-arest',
        'https://avtonom.org/news/sud-ostavil-dmitriya-ivanova-v-sizo-do-2-sentyabrya',
        'https://avtonom.org/news/roskomnadzor-razblokiroval-sayt-tor-project',
        'https://avtonom.org/news/podderzhka-politzaklyuchennyh-vecher-otkrytok-v-moskve-i-festival-v-sankt-peterburge',
        'https://avtonom.org/news/petr-ryabov-rossiyskie-anarhisty-v-2000-2015-godah',
        'https://avtonom.org/news/mosgorsud-ostavil-dmitriya-ivanova-v-sizo-0',
    ]


def test_iterate_description(get_raw_mock):
    items = list(rss.iterate_items())

    assert items[0].description[:100] == '<p>Ориентация капитализма на прибыль, а не на наши потребности со всей жестокостью проявляется во вр'
    assert items[0].description[-100:] == 'lidarnosti-s-zaklyuchennymi-anarhistami-2022-23-30-avgust/" rel="nofollow"><em>Источник</em></a></p>'
    assert items[1].description[:100] == """<p><em>Представляем вашему вниманию перевод <a target="_blank" rel="nofollow" class="twitter-timelin"""
    assert items[1].description[-100:] == """twitter-timeline-link" href="https://bristolabc.org/riptaylor/" rel="nofollow">Источник</a></em></p>"""


def test_iterate_media(get_raw_mock):
    media = [i.media for i in rss.iterate_items()]
    assert media == [
        ['https://avtonom.org/sites/default/files/store/poster2022_ru-780x1103.png'],
        ['https://avtonom.org/sites/default/files/store/taylor-768x1024.jpeg'],
        ['https://avtonom.org/sites/default/files/store/20220731_221430_0.jpg'],
        ['https://avtonom.org/sites/default/files/store/20220731_184703.jpg'],
        ['https://avtonom.org/sites/default/files/store/starship.png'],
        ['https://avtonom.org/sites/default/files/store/fiar_rus.jpg'],
        ['https://avtonom.org/sites/default/files/store/content_1.jpeg'],
        ['https://avtonom.org/sites/default/files/store/fb_img_1658957390897_1.jpg'],
        ['https://avtonom.org/sites/default/files/store/tur_anarch.jpeg'],
        ['https://avtonom.org/sites/default/files/store/20220728_192615.jpg'],
        ['https://avtonom.org/sites/default/files/store/photo_2022-04-13_16-32-03_0.jpg'],
        ['https://avtonom.org/sites/default/files/store/20220728_125837.jpg'],
        ['https://avtonom.org/sites/default/files/store/20220726_221640.jpg'],
        ['https://avtonom.org/sites/default/files/store/wrench.jpg'],
        ['https://avtonom.org/sites/default/files/store/20220723_164055.jpg'],
        ['https://avtonom.org/sites/default/files/store/20220722_200142.jpg'],
        ['https://avtonom.org/sites/default/files/store/20220722_174617.jpg'],
        ['https://avtonom.org/sites/default/files/store/20220719_191947.jpg'],
        ['https://avtonom.org/sites/default/files/store/photo_2022-02-19_13-03-31_0.jpg'],
        ['https://avtonom.org/sites/default/files/store/20220718_172606_0.jpg'],
    ]


def test_process_new_items(get_raw_mock):
    db = {}

    items = []
    rss.process_new_items(db, lambda item: items.append(item))
    assert len(items) == 20

    items = []
    rss.process_new_items(db, lambda item: items.append(item))
    assert not items

    del db['https://avtonom.org/news/petr-ryabov-rossiyskie-anarhisty-v-2000-2015-godah']
    del db['https://avtonom.org/news/poka-vse-ne-budut-svobodny-mezhdunarodnaya-nedelya-solidarnosti-s-zaklyuchennymi-anarhistami-23']
    links = []
    rss.process_new_items(db, lambda item: links.append(item.link))
    assert links == [
        'https://avtonom.org/news/petr-ryabov-rossiyskie-anarhisty-v-2000-2015-godah',
        'https://avtonom.org/news/poka-vse-ne-budut-svobodny-mezhdunarodnaya-nedelya-solidarnosti-s-zaklyuchennymi-anarhistami-23',
    ]


def test_process_new_items_exception(get_raw_mock):
    db = {}

    links = []
    def _do(item):
        if item.link == 'https://avtonom.org/news/kirillu-ukraincevu-prodlen-arest':
            raise RuntimeError()
        links.append(item.link)
    rss.process_new_items(db, _do)

    assert list(reversed(links)) == [
        'https://avtonom.org/news/poka-vse-ne-budut-svobodny-mezhdunarodnaya-nedelya-solidarnosti-s-zaklyuchennymi-anarhistami-23',
        'https://avtonom.org/freenews/achk-bristol-rip-teylor-yarost-nashe-oruzhie',
        'https://avtonom.org/news/aleksandra-skochilenko-ostanetsya-v-sizo-do-1-sentyabrya',
        'https://avtonom.org/news/v-moskve-proydet-vecher-podderzhki-antivoennyh-politzaklyuchennyh',
        'https://avtonom.org/news/sposobno-li-chelovechestvo-na-samozashchitu-trendy-poryadka-i-haosa-epizod-65-31-iyulya',
        'https://avtonom.org/blog/belarus-anarhisty-osuzhdennye-po-delu-promnya-god-v-zaklyuchenii',
        'https://avtonom.org/news/delo-o-diskreditacii-armii-protiv-evgeniya-karakasheva-prekrashcheno-za-istecheniem-sroka',
        'https://avtonom.org/news/kanskogo-podrostka-nikitu-uvarova-etapirovali-v-vospitatelnuyu-koloniyu',
        'https://avtonom.org/pages/samaya-interesnaya-strana-v-mire-blic-intervyu-s-tureckim-anarhistom',
        'https://avtonom.org/news/podelnika-tesaka-prigovorili-k-16-godam-po-delu-o-kazni-v-lesu-1',
        'https://avtonom.org/news/evgeniya-karakasheva-prodolzhat-sudit-za-diskreditaciyu-armii',
        'https://avtonom.org/news/sud-v-sankt-peterburge-rassmotrit-prodlenie-aresta-dlya-aleksandry-skochilenko',
        'https://avtonom.org/news/kinoklub-v-klube-im-dzherri-rubina-chto-v-vozduhe',
        'https://avtonom.org/news/poroshok-v-shestyorenki-sistemy-trendy-poryadka-i-haosa-epizod-64-24-iyulya',
        'https://avtonom.org/news/sud-ostavil-dmitriya-ivanova-v-sizo-do-2-sentyabrya',
        'https://avtonom.org/news/roskomnadzor-razblokiroval-sayt-tor-project',
        'https://avtonom.org/news/podderzhka-politzaklyuchennyh-vecher-otkrytok-v-moskve-i-festival-v-sankt-peterburge',
        'https://avtonom.org/news/petr-ryabov-rossiyskie-anarhisty-v-2000-2015-godah',
        'https://avtonom.org/news/mosgorsud-ostavil-dmitriya-ivanova-v-sizo-0',
    ]

    links = []
    rss.process_new_items(db, lambda item: links.append(item.link))
    assert links == [
        'https://avtonom.org/news/kirillu-ukraincevu-prodlen-arest',
    ]

    links = []
    rss.process_new_items(db, lambda item: links.append(item.link))
    assert links == []


def test_item_to_html():
    item = rss.Item('My Title', 'http://127.0.0.1/', '<p>Hello</p>', [])
    assert rss.item_to_html(item) == '<p><a href="http://127.0.0.1/">My Title</a></p><p>Hello</p>'
