import os
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

    for flight in reversed(decoded_response):
        if flight['links']['flickr']['original']:
            links.append(flight['links']['flickr']['original'])
            break

    for url in links:
        for image_url in url:
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            for image_number, image_name in enumerate(image_response.content):
                image_name = 'spacex'
                file_path = f'images/{image_number}_{image_name}.jpg'

            api_file_operations.download_images(file_path, image_url)


def main():
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    fetch_spacex_launch()


if __name__ == '__main__':
    main()
