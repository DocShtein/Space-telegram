import os
import time

import telegram
from dotenv import load_dotenv


def post_images(amount_of_time_delay, bot_token):
    bot = telegram.Bot(token=bot_token)

    while True:
        for root, dirs, files in os.walk('images'):
            for name in files:
                name = os.path.join(root, name)
                with open(name, 'rb') as photo:
                    bot.send_photo(
                        chat_id=os.getenv('CHAT_ID'), photo=photo
                    )
                time.sleep(amount_of_time_delay)


def main():
    load_dotenv()
    telegram_bot_token = os.getenv('TELEGRAM_SECRET_KEY')
    default_delay = 86400
    time_delay = int(os.getenv('TIME_DELAY_AMOUNT', default_delay))

    post_images(time_delay, telegram_bot_token)


if __name__ == '__main__':
    main()
