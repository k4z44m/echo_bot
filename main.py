from telebot import TeleBot
from telebot.types import Message

TOKEN = '6900479217:AAEdtixKM2DvkcEzFjxcJOdKJbksNu2lQ8w'

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def command_start(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    print(chat_id, user_id)
    text = 'Hi. This is bot'
    bot.send_message(chat_id, text)


@bot.message_handler(content_types=['text', 'photo', 'voice', 'sticker'])
def answer(message: Message):
    chat_id = message.chat.id
    if message.text:
        text = message.text
        if text == 'Hi':
            bot.send_message(chat_id, "Hi \U0001F603 😃. What's up?")
        else:
            bot.send_message(chat_id, text)
    if message.photo:
        photo = message.photo[0].file_id
        bot.send_photo(chat_id, photo)
    if message.voice:
        voice = message.voice.file_id
        bot.send_voice(chat_id, voice)
    if message.sticker:
        sticker = message.sticker.file_id
        bot.send_sticker(chat_id, sticker)


# Зациклим
bot.polling(non_stop=True)
