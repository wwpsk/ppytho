import telebot
import random
from telebot import types

bot = telebot.TeleBot("5857506511:AAHshDI6LusWvCDIVxFH249dRse-McgNhOY")

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open("sticker.webp", "rb")
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("😊Все команды!!!🤯 ")

    markup.add(item1,)

    bot.send_message(message.chat.id, f"Привіт я Чип, {message.from_user.first_name}!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['mem'])
def welcome(message):
    sti = open("images.jpg", "rb")
    bot.send_sticker(message.chat.id, sti)

@bot.message_handler(commands=['music'])
def send_music(message):
    audio = open("hammali-navai_-_a-esli-eto-lyubov.mp3", "rb")
    bot.send_audio(message.chat.id, audio)

@bot.message_handler(commands=['an'])
def welcome(message):
    bot.send_message(message.chat.id, "- У меня тут с женой разговор вышел... она говорит, если бы женщины правили миром, войн вообще бы не было...- А ты что?- А я ей говорю, мол, ты полностью права, ибо для ведения войны нужны стратегия и логика.- Ясно. Ну дак ты, если ночевать негде, приходи, место есть.")

@bot.message_handler(commands=['help'])
def help_command(message):
    commands = [
        "/start - Почати спілкування",
        "/mem - Відправити мем",
        "/an - Відправити анекдот",
        "/music - Відправити музику",
        "/help - Показати список команд",

    ]
    bot.send_message(message.chat.id, "Список команд:\n" + "\n".join(commands))

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text.lower() == "що робиш?":
        bot.send_message(message.chat.id, "Роблю домашку, а ти?")
    elif message.text == 'Яку оцінку сьогодні отримаєш?':
        bot.send_message(message.chat.id, str(random.randint(8, 12)))
    elif message.text == 'Як справи?':
        bot.send_message(message.chat.id, "Все добре, дякую!")
    elif message.text == 'Як Дейл':
        bot.send_message(message.chat.id, "Все добре, він пійшов гуляти!")
    elif message.text == 'Як твої друзі?':
        bot.send_message(message.chat.id, "Не дуже всі боліють")
    elif message.text == 'Коли поїдеш до пригод?':
        bot.send_message(message.chat.id, "Вже скоро!!!")
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, "Пока")
    else:
        bot.send_message(message.chat.id, "Я не розумію цю команду. Введіть /help для отримання списку команд.")

bot.polling()


