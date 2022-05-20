import os
from urllib.parse import unquote, urlsplit

import requests


def download_image(filepath, url, params=None):
    response = requests.get(url, params)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def get_image_extension(url):
    unquoted_link = unquote(url)
    parsed_url = urlsplit(unquoted_link)
    name, ext = os.path.splitext(parsed_url.path)
    return ext
