import os
import random

from dotenv import load_dotenv

import requests
import api_file_operations


def fetch_spacex_launch():
    api_url = 'https://api.spacexdata.com/v4/launches'
    response = requests.get(api_url)
    response.raise_for_status()
    decoded_response = response.json()
    if 'errors' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['errors'])

    links = []

    for flight in decoded_response:
        for _ in flight:
            if flight['links']['flickr']['original']:
                links.append(flight['links']['flickr']['original'])

    urls = random.sample(links, 1)
    api_file_operations.write_spacex_images(urls)


def main():
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    fetch_spacex_launch()


if __name__ == '__main__':
    main()
