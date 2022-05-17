import datetime
import os

import requests
from urllib.parse import urlsplit, unquote
from dotenv import load_dotenv

import api_file_operations


def get_image_extension(url):
    unquoted_link = unquote(url)
    parsed_url = urlsplit(unquoted_link)
    name, ext = os.path.splitext(parsed_url.path)
    return ext


def fetch_astronomy_picture_of_the_day(params):
    api_url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    decoded_response = response.json()
    if 'errors' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['errors'])

    links = []

    for image in decoded_response:
        try:
            links.append(image['url'])
        except KeyError:
            pass

    image_name = 'nasa_apod'

    for image_number, image_url in enumerate(links):
        file_path = f'images/{image_number}_{image_name}{get_image_extension(image_url)}'
        api_file_operations.download_image(
            file_path, image_url, params=params
        )


def fetch_earth_polychromatic_image(params):
    api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    decoded_response = response.json()
    if 'errors' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['errors'])

    for dictionary in decoded_response:
        converted_date = datetime.datetime.fromisoformat(dictionary['date'])
        formatted_date = converted_date.strftime("%Y/%m/%d")
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{dictionary["image"]}.png'
        file_path = f'images/{dictionary["image"]}.png'

        api_file_operations.download_image(
            file_path, image_url, params=params
        )


def main():
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    nasa_api_token = os.getenv('NASA_API_TOKEN')
    params = dict(api_key=nasa_api_token, count='30', thumbs=True)

    fetch_astronomy_picture_of_the_day(params)
    fetch_earth_polychromatic_image(params)


if __name__ == '__main__':
    main()
