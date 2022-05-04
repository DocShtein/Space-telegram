import os
import time
from dotenv import load_dotenv

import telegram


def post_images(amount_of_time_delay):
    telegram_bot_key = os.getenv('TELEGRAM_SECRET_KEY')
    bot = telegram.Bot(token=telegram_bot_key)
    filelist = []
    while True:
        for root, dirs, files in os.walk('images'):
            for file in files:
                filelist.append(os.path.join(root, file))
        for name in filelist:
            bot.send_document(chat_id=os.getenv('CHAT_ID'), document=open(name, 'rb'))
            time.sleep(amount_of_time_delay)


def main():
    load_dotenv()

    default_delay = 86400
    time_delay = int(os.getenv('TIME_DELAY_AMOUNT', default_delay))

    post_images(time_delay)


if __name__ == '__main__':
    main()
