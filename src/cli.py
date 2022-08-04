import dbm
import argparse

import rss
import mastodon
from session import Session


def run():
    parser = argparse.ArgumentParser(prog='avtonom_mirror')
    parser.add_argument('--db', required=True, help='path to database file')
    parser.add_argument('--server_url', required=True, help='server base URL, for example: https://mastodon.example')
    parser.add_argument('--token', required=True, help='user token (write:statuses write:media), details: https://docs.joinmastodon.org/client/authorized/#flow')
    args = parser.parse_args()

    with dbm.open(args.db, 'c') as db:
        session = Session(args.server_url, args.token)
        rss.process_new_items(db, lambda item: mastodon.publish(session, rss.item_to_html(item), item.media))
