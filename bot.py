import telebot
import random
import os

token = ""
bot = telebot.TeleBot(token)

facts = [
    "Последние годы - самые тёплые за всю историю наблюдений.",
    "Основная причина глобального потепления - деятельность человека.",
    "Ледники тают в 2 раза быстрее, чем 100 лет назад.",
    "Уровень мирового океана постоянно растёт.",
    "Леса поглощают CO₂, но их становится всё меньше."
]

tips = [
    "Выключай свет и электроприборы, когда они не нужны.",
    "Используй общественный транспорт или велосипед.",
    "Покупай меньше одноразового пластика.",
    "Экономь воду.",
    "Сортируй отходы."
]

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Привет!\n"
        "Я эко-бот\n"
        "Моя цель - рассказать о проблеме глобального потепления и о том, "
        "как каждый человек может помочь планете.\n\n"
        "Команды:\n"
        "/info - что такое глобальное потепление\n"
        "/fact - факт о климате\n"
        "/help_earth - как помочь планете\n"
        "/img - тематическое изображение"
    )

@bot.message_handler(commands=["info"])
def send_info(message):
    bot.reply_to(
        message,
        "Глобальное потепление - это постепенное повышение средней температуры Земли.\n\n"
        "Оно происходит из-за увеличения парниковых газов (CO₂, метан), "
        "которые образуются при сжигании топлива, вырубке лесов и работе заводов.\n\n"
        "Последствия:\n"
        "экстремальная жара\n"
        "наводнения\n"
        "таяние ледников"
    )

@bot.message_handler(commands=["fact"])
def send_fact(message):
    bot.reply_to(message, random.choice(facts))

@bot.message_handler(commands=["help_earth"])
def send_help(message):
    bot.reply_to(message, random.choice(tips))

@bot.message_handler(commands=["img"])
def send_img(message):
        try:
            files = os.listdir("images")
            if not files:
                return

            name = random.choice(files)
            with open(f'images/{name}', 'rb') as f:
                bot.send_photo(
                    message.chat.id,
                    f,
                    caption="Земля - наш общий дом. Береги её."
                )
        except:
            pass

bot.polling()

