import telebot
from telebot import types
import json
bot = telebot.TeleBot("6578062736:AAH-ybyQl_9x-MIjoAylOuMoOUyklNxbfa8")
with open('cafes.json','r', encoding='utf-8') as json_file:
    cafes_info=json.load(json_file)
ratings={}

@bot.callback_query_handler(func=lambda call: call.data.startswith(('up_', 'down_')))
def process_rating_callback(call):
    cafe_name = call.data.split('_')[1]  # Отримання імені кафе з даних callback

    if call.data.startswith('up_'):
        ratings[cafe_name] = ratings.get(cafe_name, 0) + 1
    elif call.data.startswith('down_'):
        ratings[cafe_name] = ratings.get(cafe_name, 0) - 1

    cafe_rating = ratings.get(cafe_name, 0)

    new_text = f"Рейтинг: {cafe_rating} 👍"

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=new_text)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Переглянути інформацію")
    item2 = types.KeyboardButton("Залишити відгук")
    markup.add(item1, item2)
    bot.reply_to(message,
                 "Привіт👋. Я телеграм бот, який допоможе тобі обрати кафе, залишити чесний відгук та дізнатись трішки більше про кожен заклад. Що тебе цікавить?",
                 reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Переглянути рейтинг")
def show_rating(message):
    rating_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for cafe_name in cafes_info:
        rating_markup.add(types.KeyboardButton(cafe_name))
    rating_markup.add(types.KeyboardButton("Назад"))
    bot.reply_to(message, "Вибери кафе, щоб побачити його рейтинг:", reply_markup=rating_markup)

import telebot
from telebot import types
import json

bot = telebot.TeleBot("6578062736:AAH-ybyQl_9x-MIjoAylOuMoOUyklNxbfa8")

# Завантаження даних з JSON-файлу
with open('cafes.json', 'r', encoding='utf-8') as json_file:
    cafes_info = json.load(json_file)

# Залишаємо ваш початковий код для обробки інших функцій

# ...

# Код для відображення інформації про кафе
@bot.message_handler(func=lambda message: message.text in cafes_info.keys())
def show_cafe_info(message):
    cafe_name = message.text
    cafe_info = cafes_info[cafe_name]
    cafe_rating = ratings.get(cafe_name, 0)
    info_text = f"Інформація про {cafe_name}:\n"
    for key, value in cafe_info.items():
        if key != "Фото":
            info_text += f"{key}: {value}\n"
    info_text += f"Рейтинг: {cafe_rating} 👍\n"
    rating_markup = types.InlineKeyboardMarkup()
    thumbs_up = types.InlineKeyboardButton("👍", callback_data=f"up_{cafe_name}")
    thumbs_down = types.InlineKeyboardButton("👎", callback_data=f"down_{cafe_name}")
    rating_markup.add(thumbs_up, thumbs_down)

    @bot.callback_query_handler(func=lambda call: call.data.startswith(('up_', 'down_')))
    def process_rating_callback(call):
        cafe_name = call.data.split('_')[1]
        if call.data.startswith('up_'):
            ratings[cafe_name] = ratings.get(cafe_name, 0) + 1
        elif call.data.startswith('down_'):
            ratings[cafe_name] = ratings.get(cafe_name, 0) - 1
        cafe_rating = ratings.get(cafe_name, 0)
        new_text = f"Рейтинг: {cafe_rating} 👍"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=new_text)
        bot.send_message(call.message.chat.id, "Дякую за вашу оцінку!")

    bot.send_photo(message.chat.id, cafe_info.get("Фото"))
    bot.reply_to(message, info_text, reply_markup=rating_markup)


@bot.message_handler(func=lambda message: message.text == "Залишити відгук")
def leave_review(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for cafe_name in cafes_info:
        markup.add(types.KeyboardButton(cafe_name))
    markup.add(types.KeyboardButton("Назад"))

    bot.reply_to(message, "Вибери кафе, для якого хочеш залишити відгук:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in cafes_info.keys())
def ask_for_review(message):
    cafe_name = message.text
    bot.reply_to(message, f"Введіть відгук для кафе '{cafe_name}':")

@bot.message_handler(func=lambda message: message.text != "Залишити відгук" and message.text != "Назад")
def save_review(message):
    cafe_name = message.text
    review = message.text
    if cafe_name in cafes_info:
        cafes_info[cafe_name]["Відгуки"].append(review)
        with open('cafes.json', 'w', encoding='utf-8') as json_file:
            json.dump(cafes_info, json_file, ensure_ascii=False, indent=4)
    markup = types.ReplyKeyboardRemove()
    bot.reply_to(message, f"Дякую за ваш відгук для кафе '{cafe_name}'!", reply_markup=markup)
    bot.send_message(message.chat.id, "Чим ще можу допомогти?")

# Завершення бота
bot.polling()

