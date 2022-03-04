# 5210218122:AAFkYPjA3JgqUq4RsK_ywz3GH4T5O-TKwAI
import telebot

TOKEN = "5210218122:AAFkYPjA3JgqUq4RsK_ywz3GH4T5O-TKwAI"

bot = telebot.TeleBot("5210218122:AAFkYPjA3JgqUq4RsK_ywz3GH4T5O-TKwAI")


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, f"Привет {message.chat.username} дружочек чем могу помогу")
    bot.send_message(message.chat.id, f"И помни я не волшебник я только учусь)")
    bot.send_message(message.chat.id, f"Слышь {message.chat.username} пришли голосовуху хочу послушать тебя")
    bot.send_message(message.chat.id, f"Или фотку.")
    bot.send_message(message.chat.id, f"Или фотку жопы))).")
    bot.send_message(message.chat.id, f"Да ладно можешь что угодно слать")
    bot.send_message(message.chat.id, f"Пошутил я)")


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Ещё раз привет!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока!')


@bot.message_handler(content_types=['text'])
def send_text2(message):
    if message.text.lower() == 'на хуй':
        bot.send_message(message.chat.id, 'Ну зачем ты так?(')
    elif message.text.lower() == 'в жопу':
        bot.send_message(message.chat.id, 'давай как лучше ты сам)')

# Обрабатываются все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    bot.send_message(message.chat.id, "Ну пиздец, что мне с эти теперь делать?")


# Обрабатываются все голосовухи
@bot.message_handler(content_types=['voice'])
def handle_docs_audio(message):
    bot.send_message(message.chat.id, ")))Голосок у тебя конечно так себе")


# Обрабатываются все фотки
@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Ну так себе фоточка если честно )))')

bot.polling(none_stop=True)
