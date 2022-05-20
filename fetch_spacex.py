import os

import requests

import api_file_operations


def fetch_spacex_launch():
    api_url = 'https://api.spacexdata.com/v4/launches'
    response = requests.get(api_url)
    response.raise_for_status()
    decoded_response = response.json()
    if 'errors' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['errors'])

    for links in reversed(decoded_response):
        urls = links['links']['flickr']['original']
        if urls:
            break

    image_name = 'spacex'

    for image_number, image_url in enumerate(urls):
        file_path = f'images/{image_number}_{image_name}{api_file_operations.get_image_extension(image_url)}'
        api_file_operations.download_image(file_path, image_url)


def main():
    os.makedirs('images', exist_ok=True)
    fetch_spacex_launch()


if __name__ == '__main__':
    main()
