import datetime
import os

import requests
from urllib.parse import urlsplit, unquote


def get_image_extension(url):
    unquoted_link = unquote(url)
    parsed_url = urlsplit(unquoted_link)
    name, ext = os.path.splitext(parsed_url.path)
    return ext


def write_spacex_images(urls_list):
    for url in urls_list:
        for image in url:
            image_response = requests.get(image)
            image_response.raise_for_status()
            for image_number, image_name in enumerate(image_response.content):
                image_name = 'spacex'
                file_path = f'images/{image_number}_{image_name}.jpg'
            with open(file_path, 'wb') as file:
                file.write(image_response.content)


def write_nasa_apod_images(url_list, params):
    for image_url in url_list:
        image_response = requests.get(image_url, params=params)
        image_response.raise_for_status()
        for image_number, image_name in enumerate(image_response):
            image_name = 'nasa_apod'
            for extension in url_list:
                filepath = f'images/{image_number}_{image_name}{get_image_extension(extension)}'
        with open(filepath, 'wb') as filepath:
            filepath.write(image_response.content)


def write_nasa_epic_images(json_response, params):
    for dictionary in json_response:
        for _ in dictionary.items():
            converted_date = datetime.datetime.fromisoformat(dictionary['date'])
            formatted_date = converted_date.strftime("%Y/%m/%d")
            image_url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{dictionary["image"]}.png'
            image_response = requests.get(image_url, params=params)
            image_response.raise_for_status()
            file_path = f'images/{dictionary["image"]}.png'
        with open(file_path, 'wb') as file:
            file.write(image_response.content)
