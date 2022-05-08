import os

import requests
from dotenv import load_dotenv

import api_file_operations


def fetch_astronomy_picture_of_the_day(params):
    api_url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    decoded_response = response.json()
    if 'errors' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['errors'])

    links = []
    try:
        for image in decoded_response:
            links.append(image['url'])
    except KeyError:
        pass

    api_file_operations.write_nasa_apod_images(links, params)


def fetch_earth_polychromatic_image(params):
    api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    decoded_response = response.json()
    if 'errors' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['errors'])

    api_file_operations.write_nasa_epic_images(decoded_response, params)


def main():
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    nasa_api_token = os.getenv('NASA_API_TOKEN')
    params = dict(api_key=nasa_api_token, count='30', thumbs=True)

    fetch_astronomy_picture_of_the_day(params)
    fetch_earth_polychromatic_image(params)


if __name__ == '__main__':
    main()
