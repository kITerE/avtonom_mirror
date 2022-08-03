import requests
import xml.etree.ElementTree as ET

from collections import namedtuple


def get_raw():
    r = requests.get('https://avtonom.org/rss_full')
    r.raise_for_status()
    return r.text


Item = namedtuple('Item', ('title', 'link', 'description', 'media'))


def iterate_items():
    for root_child in ET.fromstring(get_raw()):
        if root_child.tag == 'channel':
            for channel_child in root_child:
                if channel_child.tag == 'item':
                    as_dict = {i.tag: i for i in channel_child}

                    media = []
                    if 'enclosure' in as_dict:
                        media.append(as_dict['enclosure'].attrib.get('url'))

                    yield Item(as_dict['title'].text, as_dict['link'].text,
                               as_dict['description'].text.strip(), media)
            break


def iterate_new_items(db):
    for item in iterate_items():
        if db.get(item.link):
            continue
        yield item
        db[item.link] = True


def item_to_html(item):
    p = ET.Element('p')
    a = ET.SubElement(p, 'a')
    a.attrib.update(href=item.link)
    a.text = item.title
    return ET.tostring(p, encoding="unicode") + item.description
