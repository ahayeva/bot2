import telebot
from telebot import types

bot = telebot.TeleBot("6578062736:AAH-ybyQl_9x-MIjoAylOuMoOUyklNxbfa8")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Поставити оцінку")
    item2 = types.KeyboardButton("Переглянути рейтинг")
    item3 = types.KeyboardButton("Переглянути інформацію про кафе")
    markup.add(item1, item2, item3)
    bot.reply_to(message,
                 "Привіт👋. Я телеграм бот, який допоможе тобі обрати кафе, залишити чесний відгук та дізнатись трішки більше про кожен заклад. Що тебе цікавить?",
                 reply_markup=markup)
cafes_info = {
      "Соціальне християнське кафе\"Витанія\"": {
          "Адреса":"вулиця Чорновола,4",
          "Телефон":"+38 (096) 521-83-25",
          "Години роботи":"Пн-Нд: 11:00-20:00",
          "Про заклад":"Соціальне Християнське Кафе Витанія   Українська Кухня   Банкетний Зал До 100 Осіб   Доставка Піци   Доставка Їжі   Кафе, бари, кафетерії   Піцерії   Кафе   Бар   Кафетерійний відділ   Кафетерій   Піцерія   Піца   Піцца   Весілля   Весільні зали   Весільні фуршети   Весільний стіл оформлення   День народження   Зал для весілля   Зали для весілля   Кафе витанія   Корпоративи   Меню на весілля   Новорічні корпоративи   Новорічний корпоратив   Оформлення весільного столу   Оформлення козацького столу на весіллі   Оформлення фуршетних столів на весілля   Оформлення фуршетного столу на весілля   Побачення   Поминки   Святкування дня народження дитини",
          "Фото":"C:/Users/HP/Desktop/cafe_photos/Соціальне християнське кафе Витанія.jpg",

      },
     "Суші Бар\"Тіта\"":{
         "Адреса":"вулиця Мала,1",
          "Телефон":"+38 (063) 831-17-77",
          "Години роботи":"Пн-Нд:11:00-23:00",
          "Про заклад":"Страви японської,паназійської та авторської кухонь.Доставка їжі по місту.",
          "Фото":"C:/Users/HP/Desktop/cafe_photos/Суші-бар Тіта.jpg"
    },
    "Тареля":{
          "Адреса":"вулиця Шевченка,1",
          "Телефон":"+38 (067) 900-77-05",
          "Години роботи":"Пн-Пт: 09:00-22:00, Сб-Нд:09:00-23:00",
          "Про заклад":"Страви італійської, української, європейської та азіатської кухні.Доставка їжі",
          "Фото":"C:/Users/HP/Desktop/cafe_photos/Тареля.jpg"
},
    "Сосновий бір":{
        "Адреса":"вулиця Курортна,11",
        "Телефон":"+38 (067) 673-53-54",
        "Години роботи":"Пн-Нд:12:00- 22:30",
        "Про заклад":"Ресторан «Сосновий бір» запрошує на святкування бенкетів, днів народжень, ювілеїв та інших подій. У нас подають ароматні й дуже смачні страви української та європейської кухні, а також готуємо соковиті страви на мангалі.",
        "Фото":"C:/Users/HP/Desktop/cafe_photos/Сосновий бір.jpg"
    },
    "Майстерня їжі TARANTINO":{
        "Адреса":"вулиця Івана Мазепи,8",
        "Телефон":"+38 (097) 307-30-07",
        "Години роботи":"Пн-Нд: 10:00-23:00",
        "Про заклад":"Смачні страви італійської,паназійської та української кухонь,піца,суші. Доставка їжі",
        "Фото":"C:/Users/HP/Desktop/cafe_photos/Майсерня їжі TARANTINO.jpg"
    },
    "Ресторан-піцерія Green Park":{
        "Адреса":"вулиця Лепкого, 2",
        "Телефон":"+38(050) 533-93-74",
        "Години роботи":"Пн-НдЖ: 11:00-22:00",
        "Про заклад":"Ресторан-піцерія «Green Park Pizza & Rest» — заклад, що знаходиться у самому центрі міста та дарує для відвідувачів можливість смачно поїсти й відпочити у комфортній атмосфері",
        "Фото":"C:/Users/HP/Desktop/cafe_photos/Ресторан-піцерія Green Park.jpg"
    },
    "Ресторан Корчма на Заліссі":{
"Адреса":"вулиця Завіжна,121",
        "Телефон":"+38 (097) 305-34-71",
        "Години роботи":"Пн-Нд: 12:00-21:00",
        "Про заклад":"Ресторан «Корчма» розташований на території відпочинкового комплексу Залісся та є ідеальним місцем для незабутніх святкувань найважливіших подій в житті.Заклад має дуже вдале розташування — на березі озера, відокремлений від міської метушні й гамору. Тому час, проведений тут, буде сповнений приємних розваг, цікавого спілкування, якісного дозвілля на свіжому повітрі.",
        "Фото":"C:/Users/HP/Desktop/cafe_photos/Ресторан Корчма на Заліссі.jpg"
    },
"ПАБ Солік":{
"Адреса":"вулиця Зелений ставок,23",
        "Телефон":"+38 (097) 981-55-69",
        "Години роботи":"Пн-Нд: 11:00-22:00",
        "Про заклад":"Хочеш зарядитись енергією і позитивом, скуштувати неймовірно смачні страви української кухні та поринути в приємну домашню атмосферу?Тоді, завітай у паб «Солік»!Цей заклад є ідеальним місцем для посиденьок у великій компанії друзів! А ще, в нас можна організувати святкування днів народжень та інших подій.",
        "Фото":"C:/Users/HP/Desktop/cafe_photos/ПАБ Солік.jpg"
},
"Піцерія бістро Bus Station":{
"Адреса":"вулиця Орлика,11",
        "Телефон":"+38 (098) 309-55-95",
        "Години роботи":"Пн-Нд: 08:00-20:00",
        "Про заклад":"Смачні страви української кухні, піца. Святкування урочистих подій",
        "Фото":"C:/Users/HP/Desktop/cafe_photos/Піцерія-бістро Bus Station.jpg"
},
"Піцерія Chicago Style":{
"Адреса":"майдан Шевченка,1",
        "Телефон":"+38 (097) 041-26-26",
        "Години роботи":"Пн- Нд: 10:00-23:00",
        "Про заклад":"Коли ви наступного разу скажете друзям: йдемо на піцу, то ми вас чекаємо в піцерії «Chicago Style». Це затишний заклад відповідає міжнародним стандартам НАСР. Тут можна відпочити з друзями та смачно поїсти.",
        "Фото":"C:/Users/HP/Desktop/cafe_photos/Піцерія Chicago Style.jpg"
},
"Кафе Тет-а-тет":{
"Адреса":"вулиця Михайла Грушевського,77",
        "Телефон":"+38 (096) 815-93-76",
        "Години роботи":"Пн-Нд: 11:00-23:00",
        "Про заклад":"Смачна піца. Страви української кухні. Банкетний зал до 25 осіб, два VIP-зали до 10 і 8 осіб. Можливість доставки їжі.",
        "Фото":"C:/Users/HP/Desktop/cafe_photos/Кафе Тет-а-тет.jpg"
},
"Кафе Налисник":{
"Адреса":"вулиця Михайла Грушевського,44/3",
        "Телефон":"+38 (068) 510-50-51",
        "Години роботи":"Пн-Нд: 09:00-22:00",
        "Про заклад":"Смачні страви швидкого приготування",
        "Фото":"C:/Users/HP/Desktop/cafe_photos/Кафе Налисник.jpg"
},
"Кафе Мальви":{
"Адреса":"вулиця Бориславська,6",
        "Телефон":"+38 (097) 239-61-40",
        "Години роботи":"Пн-Нд: 11:00-23:00",
        "Про заклад":"Запрошуємо вас завітати в кафе «Мальви» та скоштувати страви традиційної української кухні.Витриманий інтер'єр у народному стилі зі збереженням автентичних елементів створює особливий настрій. Тут ви можете весело провести час та відпочити від напружених буднів. «Мальви» — ідеальне місце, щоб відсвяткувати важливу подію вашого життя: весілля, день народження, корпоратив, хрестини. Ми допоможемо організувати все так, щоб ви та ваші гості залишились задоволеними. Складемо меню з урахуванням ваших смаків та побажань",
        "Фото":"C:/Users/HP/Desktop/cafe_photos/Кафе Мальви.jpg"
},
"Franko beef&burger":{
        "Адреса":"вулиця Площа ринок,3",
        "Телефон":"+38(067) 772-79-77",
        "Години роботи":"Пн-Чт: 10:00-23:00, Пт-Нд: 10:00-24:00",
        "Про заклад":"Страви європейської кухні",
        "Фото":"C:/Users/HP/Desktop/cafe_photos/Franko beef&burger.jpg"
}
}

ratings = {cafe: {"👍": 0, "👎": 0} for cafe in cafes_info}


def generate_cafe_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for cafe in cafes_info.keys():
        markup.add(types.KeyboardButton(cafe))
    return markup


def generate_rating_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("👍", "👎")
    return markup





@bot.message_handler(func=lambda message: message.text == "Переглянути інформацію про кафе")
def view_cafes_info(message):
    markup = generate_cafe_buttons()
    bot.send_message(message.chat.id, "Обери кафе, щоб переглянути інформацію:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in cafes_info.keys())
def display_cafe_info(message):
    cafe_name = message.text
    cafe_info = cafes_info.get(cafe_name, "Інформація відсутня")
    photo_path = cafe_info.get("Фото", )

    markup = generate_rating_buttons()
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=f"Вибрано: {cafe_name}. Залиште свою оцінку:\n\n{cafe_info}",
                       reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Поставити оцінку")
def rate_cafe(message):
    markup = generate_cafe_buttons()
    bot.send_message(message.chat.id, "Обери кафе для оцінювання:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Переглянути рейтинг")
def view_ratings(message):
    markup = generate_cafe_buttons()
    bot.send_message(message.chat.id, "Обери кафе для перегляду рейтингу:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in cafes_info.keys())
def display_ratings(message):
    cafe_name = message.text
    if cafe_name in ratings:
        positive = ratings[cafe_name]["👍"]
        negative = ratings[cafe_name]["👎"]
        bot.reply_to(message, f"Заклад '{cafe_name}' отримав:\n👍 {positive}, 👎 {negative}")
    else:
        bot.reply_to(message, f"У закладу '{cafe_name}' ще немає оцінок.")


@bot.message_handler(func=lambda message: message.text in ["👍", "👎"])
def handle_rating(message):
    cafe_name = message.reply_to_message.caption.splitlines()[0][9:]
    if cafe_name in cafes_info:
        rating = message.text
        ratings[cafe_name][rating] += 1
        bot.reply_to(message, "Дякуємо за вашу оцінку ☺️")
    else:
        bot.reply_to(message, "Щось пішло не так. Будь ласка, спробуйте ще раз.")
bot.infinity_polling()














# @bot.message_handler(func=lambda message: message.text == "Переглянути рейтинг")
# def view_ratings(message):
#     markup = generate_cafe_buttons()
#     bot.send_message(message.chat.id, "Обери кафе для перегляду рейтингу:", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text in cafes_info.keys())
# def display_ratings(message):
#     cafe_name = message.text
#     if cafe_name in ratings:
#         positive = ratings[cafe_name]["👍"]
#         negative = ratings[cafe_name]["👎"]
#         bot.reply_to(message, f"Заклад '{cafe_name}' отримав:\n👍 {positive}, 👎 {negative}")
#     else:
#         bot.reply_to(message, f"У закладу '{cafe_name}' ще немає оцінок.")
#
# @bot.message_handler(func=lambda message: message.text in ["👍", "👎"])
# def handle_rating(message):
#     cafe_name = message.reply_to_message.caption.splitlines()[0][9:]
#     if cafe_name in cafes_info:
#         rating = message.text
#         ratings[cafe_name][rating] += 1
#         bot.reply_to(message, "Дякуємо за вашу оцінку ☺️")
#     else:
#         bot.reply_to(message, "Щось пішло не так. Будь ласка, спробуйте ще раз.")
#
# bot.infinity_polling()
# ratings = {}
#
#
# def generate_cafe_buttons():
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     for cafe_name in cafes_info.keys():
#         markup.add(types.KeyboardButton(cafe_name))
#     return markup
#
# def generate_rating_buttons():
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.row("👍", "👎")
#     return markup
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     markup = generate_cafe_buttons()
#     bot.reply_to(message, "Привіт👋. Я телеграм бот, який допоможе тобі обрати кафе, залишити чесний відгук та дізнатись трішки більше про кожен заклад. Що тебе цікавить?", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text == "Переглянути інформацію про кафе")
# def view_cafes_info(message):
#     markup = generate_cafe_buttons()
#     bot.send_message(message.chat.id, "Обери кафе, щоб переглянути інформацію:", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text in cafes_info.keys())
# def display_cafe_info(message):
#     cafe_name = message.text
#     cafe_info = cafes_info.get(cafe_name, "Інформація відсутня")
#     photo_path = cafe_info.get("Фото", default_photo_path)
#
#     markup = generate_rating_buttons()
#     bot.send_photo(message.chat.id, photo_path, caption=f"Вибрано: {cafe_name}. Залиште свою оцінку:\n\n{cafe_info}", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text == "Поставити оцінку")
# def rate_cafe(message):
#     markup = generate_cafe_buttons()
#     bot.send_message(message.chat.id, "Обери кафе для оцінювання:", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text == "Переглянути рейтинг")
# def view_ratings(message):
#     markup = generate_cafe_buttons()
#     bot.send_message(message.chat.id, "Обери кафе для перегляду рейтингу:", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text in cafes_info.keys())
# def display_ratings(message):
#     cafe_name = message.text
#     if cafe_name in ratings:
#         positive = ratings[cafe_name]["👍"]
#         negative = ratings[cafe_name]["👎"]
#         bot.reply_to(message, f"Заклад '{cafe_name}' отримав:\n👍 {positive}, 👎 {negative}")
#     else:
#         bot.reply_to(message, f"У закладу '{cafe_name}' ще немає оцінок.")
#
# @bot.message_handler(func=lambda message: message.text in ["👍", "👎"])
# def handle_rating(message):
#     cafe_name = message.reply_to_message.caption.splitlines()[0][9:]
#     if cafe_name in cafes_info:
#         rating = message.text
#         if cafe_name not in ratings:
#             ratings[cafe_name] = {"👍": 0, "👎": 0}
#         ratings[cafe_name][rating] += 1
#         bot.reply_to(message, "Дякуємо за вашу оцінку ☺️")
#     else:
#         bot.reply_to(message, "Щось пішло не так. Будь ласка, спробуйте ще раз.")
#
# bot.infinity_polling()
# #
# def generate_cafe_buttons():
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     for cafe_name in cafes_info.keys():
#         markup.add(types.KeyboardButton(cafe_name))
#     return markup
#
# def generate_rating_buttons():
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.row("👍", "👎")
#     return markup
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     markup = generate_cafe_buttons()
#     bot.reply_to(message, "Привіт👋. Я телеграм бот, який допоможе тобі обрати кафе, залишити чесний відгук та дізнатись трішки більше про кожен заклад. Що тебе цікавить?", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text == "Переглянути інформацію про кафе")
# def view_cafes_info(message):
#     markup = generate_cafe_buttons()
#     bot.send_message(message.chat.id, "Обери кафе, щоб переглянути інформацію:", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text in cafes_info.keys())
# def display_cafe_info(message):
#     cafe_name = message.text
#     cafe_info = cafes_info.get(cafe_name, "Інформація відсутня")
#     photo_path = cafe_info.get("Фото", default_photo_path)
#
#     markup = generate_rating_buttons()
#     bot.send_photo(message.chat.id, photo_path, caption=f"Вибрано: {cafe_name}. Залиште свою оцінку:\n\n{cafe_info}", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text == "Поставити оцінку")
# def rate_cafe(message):
#     markup = generate_cafe_buttons()
#     bot.send_message(message.chat.id, "Обери кафе для оцінювання:", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text == "Переглянути рейтинг")
# def view_ratings(message):
#     markup = generate_cafe_buttons()
#     bot.send_message(message.chat.id, "Обери кафе для перегляду рейтингу:", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text in cafes_info.keys())
# def display_ratings(message):
#     cafe_name = message.text
#     if cafe_name in ratings:
#         positive = ratings[cafe_name]["👍"]
#         negative = ratings[cafe_name]["👎"]
#         bot.reply_to(message, f"Заклад '{cafe_name}' отримав:\n👍 {positive}, 👎 {negative}")
#     else:
#         bot.reply_to(message, f"У закладу '{cafe_name}' ще немає оцінок.")
# @bot.message_handler(func=lambda message: message.text in ["👍", "👎"])
# def handle_rating(message):
#     cafe_name = message.reply_to_message.caption.splitlines()[0][9:]
#     if cafe_name in cafes_info:
#         rating = message.text
#         ratings[cafe_name][rating] += 1
#         bot.reply_to(message, "Дякуємо за вашу оцінку ☺️")
#     else:
#         bot.reply_to(message, "Щось пішло не так. Будь ласка, спробуйте ще раз.")
#
#
# bot.infinity_polling()



# def rate_cafes(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     cafes = [
#         "Кафе\"Мальви\"",
#         "Кафе\"У Надії\"",
#         "Соціальне християнське кафе Витанія",
#         "Сосновий бір",
#         "Cуші-бар ТІТА",
#         "Кафе Мальви",
#         "Майстерня їжі TARANTINO",
#         "Гастро - кав'ярня Кавун ",
#         "Кафе Тет-а-тет",
#         "Відпочинковий центр Zefir",
#         "ПАБ Солік",
#         "Кафе\"Налисник\"",
#         "Піцерія Chicago Style",
#         "Піцерія - бістро Bus Station",
#         "Кафе Налисник",
#         "Ресторан Корчма на Заліссі",
#         "Відпочинковий комплекс Золота гора"
#         "Ресторан - піцерія Green Park",
#         "Franko beef&burger",
#         "Тареля"
#
#     ]
#     for cafe in cafes:
#         markup.add(types.KeyboardButton(cafe))
# ratings = {cafe: {"👍": 0, "👎": 0} for cafe in cafes_info}
#
#
# def generate_cafe_buttons():
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     for cafe in cafes_info.keys():
#         markup.add(types.KeyboardButton(cafe))
#     return markup
#
#
# def generate_rating_buttons():
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.row("👍", "👎")
#     return markup
#
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton("Поставити оцінку")
#     item2 = types.KeyboardButton("Переглянути рейтинг")
#     item3 = types.KeyboardButton("Переглянути інформацію про кафе")
#     markup.add(item1, item2, item3)
#     bot.reply_to(message,
#                  "Привіт👋. Я телеграм бот, який допоможе тобі обрати кафе, залишити чесний відгук та дізнатись трішки більше про кожен заклад. Що тебе цікавить?",
#                  reply_markup=markup)
#
#
# @bot.message_handler(func=lambda message: message.text == "Переглянути інформацію про кафе")
# def view_cafes_info(message):
#     markup = generate_cafe_buttons()
#     bot.send_message(message.chat.id, "Обери кафе, щоб переглянути інформацію:", reply_markup=markup)
#
#
# @bot.message_handler(func=lambda message: message.text in cafes_info.keys())
# def display_rate_cafe(message):
#     cafe_name = message.text
#     cafe_info = rate_cafes().get(cafe_name, "Інформація відсутня")
#     photo_path = cafe_info.get("Фото", "C:/Users/HP/Desktop/cafe_photos/Соціальне християнське кафе Витанія.jpg")
#
#     markup = generate_rating_buttons()
#     with open(photo_path, 'rb') as photo:
#         bot.send_photo(message.chat.id, photo, caption=f"Вибрано: {cafe_name}. Залиште свою оцінку:\n\n{cafe_info}",
#                        reply_markup=markup)
#
#
# @bot.message_handler(func=lambda message: message.text == "Поставити оцінку")
# def rate_cafe(message):
#     markup = generate_cafe_buttons()
#     bot.send_message(message.chat.id, "Обери кафе для оцінювання:", reply_markup=markup)
#
#
# @bot.message_handler(func=lambda message: message.text == "Переглянути рейтинг")
# def view_ratings(message):
#     markup = generate_cafe_buttons()
#     bot.send_message(message.chat.id, "Обери кафе для перегляду рейтингу:", reply_markup=markup)
#
#
# @bot.message_handler(func=lambda message: message.text in cafes_info.keys())
# def display_ratings(message):
#     cafe_name = message.text
#     if cafe_name in ratings:
#         positive = ratings[cafe_name]["👍"]
#         negative = ratings[cafe_name]["👎"]
#         bot.reply_to(message, f"Заклад '{cafe_name}' отримав:\n👍 {positive}, 👎 {negative}")
#     else:
#         bot.reply_to(message, f"У закладу '{cafe_name}' ще немає оцінок.")
#
#
# @bot.message_handler(func=lambda message: message.text in ["👍", "👎"])
# def handle_rating(message):
#     cafe_name = message.reply_to_message.caption.splitlines()[0][9:]
#     if cafe_name in cafes_info:
#         rating = message.text
#         ratings[cafe_name][rating] += 1
#         bot.reply_to(message, "Дякуємо за вашу оцінку ☺️")
#     else:
#         bot.reply_to(message, "Щось пішло не так. Будь ласка, спробуйте ще раз.")
#
#
# bot.infinity_polling()
#

#








#
# ratings = {}
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton("Поставити оцінку")
#     item2 = types.KeyboardButton("Переглянути оцінки")
#     item3 = types.KeyboardButton("Переглянути інформацію про кафе")
#     markup.add(item1, item2,item3)
#     bot.reply_to(message, "Привіт👋. Я телеграм бот який допоможе тобі обрати кафе, залишити чесний відгук та дізнатись трішки більше про кожен заклад."
#                           "Що тебе цікавить?", reply_markup=markup)
#
# def rate_cafes(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     cafes = [
#         "Соціальне християнське кафе \"Витанія\"",
#         "Кафе \"Гама\"",
#         "Cуші-бар\"ТІТА\"",
#         "Кафе\"Мальви\"",
#         "Кафе\"Люкс\"",
#         "Піцерія\"TARANTINO\"",
#         "Кафе - їдальня\"Юність\"",
#         "Кафе\"Жароманія\"",
#         "Гастро - кав'ярня\"Кавун\"",
#         "Кафе\"Тет-а-тет\"",
#         "Кафе\"Час поїсти\"",
#         "Бар\"Paradox\"",
#         "Відпочинковий центр\"Zefir\"",
#         "ПАБ\"Солік\"",
#         "Кафе\"У Надії\"",
#         "BBQ\"Na Stini\"",
#         "Заклад швидкого харчування\"I love kebab\"",
#         "Арт - клуб\"82100\"",
#         "Кафе\"Алібі\"",
#         "Соціальне християнське кафе Витанія",
#         "Сосновий бір",
#         "Cуші-бар ТІТА",
#         "Кафе Мальви",
#         "Майстерня їжі TARANTINO",
#         "Гастро - кав'ярня Кавун ",
#         "Кафе Тет-а-тет",
#         "Кафе Час поїсти",
#         "Бар Paradox",
#         "Відпочинковий центр Zefir",
#         "ПАБ Солік",
#         "Кафе У Надії",
#         "BBQ Na Stini",
#         "Заклад швидкого харчування I love kebab",
#         "Арт - клуб 82100",
#         "Кафе Алібі",
#         "pizza Simka sushi",
#         "Wokmer",
#         "Піцерія\"Chicago Style\"",
#         "Піцерія - бістро\"Bus Station\"",
#         "Кафе\"Гостинний двір\"",
#         "Кафе\"Налисник\"",
#         "Банкетний зал\"Фортуна\"",
#         "Кафе\"Вінзарня\"",
#         "Gastro pub\"KABINET\"",
#         "Ресторан\"Корчма на Заліссі\"",
#         "Відпочинковий комплекс\"Золота гора\""
#         "Ресторан - піцерія\"Green Park\"",
#         "Бар\"Beer Club\""
#         "Піцерія Chicago Style",
#         "Піцерія - бістро Bus Station",
#         "Кафе Гостинний двір",
#         "Кафе Налисник",
#         "Банкетний зал Фортуна",
#         "Кафе Вінзарня",
#         "Gastro pub KABINET",
#         "Ресторан Корчма на Заліссі",
#         "Відпочинковий комплекс Золота гора"
#         "Ресторан - піцерія Green Park",
#         "Бар Beer Club",
#         "Franko beef&burger",
#         "Тареля"
#
#     ]
#     for cafe in cafes:
#         markup.add(types.KeyboardButton(cafe))
# def rate_selected_cafe(message):
#
#     photo_filename = cafe_name.replace(" ", "_").lower() + ".jpg"
#     photo_url = f"URL_ПАПКИ_З_ФОТО/{photo_filename}"
#     photo_url = (f"BBQ Na Stini"
#                  f"/{photo_filename}")
#     bot.send_photo(message.chat.id, photo_url, f"Ваша оцінка для {cafe_name}:", reply_markup=markup)
#
#
# @bot.message_handler(func=lambda message: message.text.startswith("Залишити оцінку"))
# def handle_rating_selection(message):
#     _, cafe_name, rating_symbol = message.text.split()
#     if cafe_name in ratings:
#         if rating_symbol == "👍":
#             ratings[cafe_name]["positive"] += 1
#         elif rating_symbol == "👎":
#             ratings[cafe_name]["negative"] += 1
#     else:
#         if rating_symbol == "👍":
#             ratings[cafe_name] = {"positive": 1, "negative": 0}
#         elif rating_symbol == "👎":
#             ratings[cafe_name] = {"positive": 0, "negative": 1}
#
#     bot.reply_to(message, "Дякую за вашу оцінку!")
#
# @bot.message_handler(func=lambda message: message.text.startswith("Переглянути оцінки"))
# def handle_view_ratings(message):
#     cafe_name = message.text.split()[-1]
#     if cafe_name in ratings:
#         positive = ratings[cafe_name]["positive"]
#         negative = ratings[cafe_name]["negative"]
#         bot.reply_to(message, f"Оцінки для {cafe_name}:\n👍 {positive}  👎 {negative}")
#     else:
#         bot.reply_to(message, f"Для {cafe_name} ще немає оцінок.")
# bot.infinity_polling()