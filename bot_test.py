# bot_test.py

import requests

TOKEN = '7201210943:AAHhoxs4ph7D-n3SsPDcK3UcmhIggUWUZ9I'
CHAT_ID = 7218673104 # ← сюда вставь свой Telegram ID
TEXT = 'Привет от бота! 🤖'

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
params = {
    'chat_id': CHAT_ID,
    'text': TEXT
}

response = requests.get(url, params=params)
print(response.json())

