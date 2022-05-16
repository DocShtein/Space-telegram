import requests


def download_images(filepath, image_url, params=None):
    image_response = requests.get(image_url, params)
    image_response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(image_response.content)
