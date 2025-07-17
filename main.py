# client_api/main.py

from pyrogram import Client

api_id =22522618     # ← сюда вставь свой api_id (без кавычек)
api_hash = "0b35cfd6260ddecade78dad829895b1d"  # ← сюда вставь свой api_hash (в кавычках)

app = Client("my_account", api_id=api_id, api_hash=api_hash)

app.start()
app.send_message("me", "Привет, это я! 🤖")
app.stop()
