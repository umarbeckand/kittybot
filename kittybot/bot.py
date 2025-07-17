import requests
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater

# 🔐 Токен бота (замени на свой! Никому не показывай в продакшене)
TOKEN = '7201210943:AAHhoxs4ph7D-n3SsPDcK3UcmhIggUWUZ9I'

# 🐱 URL API для получения случайной картинки кота
CAT_API_URL = 'https://api.thecatapi.com/v1/images/search'

# 🧠 Функция получения картинки кота
def get_new_image():
    response = requests.get(CAT_API_URL).json()
    return response[0].get('url')


# 🚀 Команда /start
def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name

    # Кнопка /newcat
    button = ReplyKeyboardMarkup([['/newcat']], resize_keyboard=True)

    # Приветствие
    context.bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {name}! Вот тебе котик 🐱',
        reply_markup=button
    )
    # Фото котика
    context.bot.send_photo(chat.id, get_new_image())


# 🐾 Команда /newcat
def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


# ⚙️ Запуск бота
def main():
    print("▶️ Бот запускается...")
    updater = Updater(token=TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', wake_up))
    dp.add_handler(CommandHandler('newcat', new_cat))

    updater.start_polling()
    print("✅ Бот работает. Нажми Ctrl+C для остановки.")
    updater.idle()


if __name__ == '__main__':
    main()
