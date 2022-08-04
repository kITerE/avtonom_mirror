import tempfile
import requests


def post_media(session, media_url):
    r = requests.get(media_url, stream=True)
    r.raise_for_status()

    with tempfile.TemporaryFile() as f:
        for chunk in r.iter_content(chunk_size=8 * 1024 * 1024):
            if chunk:
                f.write(chunk)

        f.seek(0)

        r = session.do('post', 'api/v1/media', files=dict(file=f))
        return r['id']


def publish(session, content, media):
    media_ids = [post_media(session, url) for url in media]
    r = session.do('post', 'api/v1/statuses',
                   data=dict(status=content, content_type='text/html', media_ids=media_ids))
    return r['id']
