import datetime
import os
from dotenv import load_dotenv

import requests
from urllib.parse import urlsplit, unquote


def create_directory(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def get_image_extension(link):
    unquoted_link = unquote(link)
    parsed_url = urlsplit(unquoted_link)
    file_extension = os.path.splitext(parsed_url.path)
    file_extension_index = 1
    return file_extension[file_extension_index]


def fetch_astronomy_picture_of_the_day(token):
    api_url = 'https://api.nasa.gov/planetary/apod'
    params = dict(api_key=token, count='30', thumbs=True)
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

    for image_url in links:
        image_response = requests.get(image_url, params=params)
        image_response.raise_for_status()
        for image_number, image_name in enumerate(image_response):
            image_name = 'nasa_apod'
            for extension in links:
                filepath = f'images/{image_number}_{image_name}{get_image_extension(extension)}'
        with open(filepath, 'wb') as filepath:
            filepath.write(image_response.content)


def fetch_earth_polychromatic_image(token):
    api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = dict(api_key=token)
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    decoded_response = response.json()
    if 'errors' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['errors'])

    for dictionary in decoded_response:
        for _ in dictionary.items():
            converted_date = datetime.datetime.fromisoformat(dictionary['date'])
            formatted_date = converted_date.strftime("%Y/%m/%d")
            image_url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{dictionary["image"]}.png'
            image_response = requests.get(image_url, params=params)
            image_response.raise_for_status()
            file_path = f'images/{dictionary["image"]}.png'
        with open(file_path, 'wb') as file:
            file.write(image_response.content)


def main():
    load_dotenv()
    create_directory('images')
    nasa_api_token = os.getenv('NASA_API_TOKEN')

    fetch_astronomy_picture_of_the_day(nasa_api_token)
    fetch_earth_polychromatic_image(nasa_api_token)


if __name__ == '__main__':
    main()
