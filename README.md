# Space Telegram

The scripts: **fetch_nasa.py**, **fetch_spacex.py** and **post_images.py** allows you to upload various photos of space and post on your Telegram channel.
The scripts use the following APIs: 
1. [SpaceX](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1) 
2. [Astronomy Picture of the Day (APOD)](https://api.nasa.gov/#apod)
3. [Earth Polychromatic Imaging Camera (EPIC)](https://api.nasa.gov/#epic) 
4. [Telegram bot API](https://core.telegram.org/bots/api)

### How to install

1. [Register on the NASA website](https://api.nasa.gov/#signUp) and get the API key.
2. Paste the copied key into the **.env** file as shown below:
```
NASA_API_TOKEN = "place you API key here"
```
3. How to get Telegram bot API token:
* **Step 1:** Find telegram bot named "@botfarther" in Telegram application, he will help you with creating and managing your bot.
* **Step 2:** Print “/help” and you will see all possible commands that the botfather can operate.
* **Step 3:** To create a new bot type “/newbot” or click on it. Follow instructions he given and create a new name to your bot. If you are making a bot only for experimentation, as it has to be a unique name, you can use namespace your bot by placing your name before it in its username. By the way, its screen name can be anything you like.

4. Paste the copied Telegram API token into the **.env** file as shown below:
```
TELEGRAM_SECRET_KEY = 'place your Telegram API token here'
```

5. Paste your Telegram chat id into the **.env** file as shown below:
```
CHAT_ID = 'place your chat id here'
```
6. Make a telegram bot an administrator of your channel.

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use

1. Run **fetch_nasa.py** and **fetch_spacex.py** to get images.
2. Run **post_images.py** to post fetched images on your Telegram channel.
3. You can change the delay time for publishing images in a Telegram channel by changing the value (**in seconds**) of the environment variable **TIME_DELAY_AMOUNT** in the **.env** file. The default value is **86400**.

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).