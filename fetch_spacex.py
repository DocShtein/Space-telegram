import os
import random
from dotenv import load_dotenv

import requests


def create_directory(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def fetch_spacex_launch():
    api_url = 'https://api.spacexdata.com/v4/launches'
    response = requests.get(api_url)
    response.raise_for_status()
    decoded_response = response.json()
    if 'errors' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['errors'])
    random_spacex_launch = random.randint(0, 172)
    links = decoded_response[random_spacex_launch]['links']['flickr']['original']

    for url in links:
        image_response = requests.get(url)
        image_response.raise_for_status()
        for image_number, image_name in enumerate(image_response.content):
            image_name = 'spacex'
            file_path = f'images/{image_number}_{image_name}.jpg'
        with open(file_path, 'ab') as file:
            file.write(image_response.content)


def main():
    load_dotenv()
    create_directory('images')


if __name__ == '__main__':
    main()
