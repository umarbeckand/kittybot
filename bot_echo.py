# bot_echo.py

import time
import requests

TOKEN = 'твой_токен_бота'
URL = f'https://api.telegram.org/bot{TOKEN}/'
last_update_id = 0

while True:
    updates = requests.get(URL + 'getUpdates', params={'offset': last_update_id + 1}).json()

    for update in updates['result']:
        chat_id = update['message']['chat']['id']
        text = update['message'].get('text', '')

        requests.get(URL + 'sendMessage', params={
            'chat_id': chat_id,
            'text': f'Ты сказал: {text}'
        })

        last_update_id = update['update_id']
    
    time.sleep(2)
