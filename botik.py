import telebot
import program
from programs import specialization_chest, specialization_legs, specialization_arms, specialization_shoulders, specialization_back, body_3x, body_4x

bot = telebot.TeleBot("8366220571:AAEzYkmpco4Omc5qEWRbkVcgZASulBzDLCU")

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton('Пройти анкету', callback_data='prog')
    markup.row(btn1)
    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! 💪\n"
    "Я — твой персональный бот-тренер, и моя цель — помочь тебе стать сильнее, красивее и круче! 🚀\n"
    "Всего пару вопросов — и я подберу для тебя программу тренировок, которая реально работает.\n"
    "Готов начать путь к новым результатам? 🔥",
        reply_markup = markup)

@bot.message_handler(commands=['back'])
def back(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton('Пройти анкету', callback_data='prog')
    markup.row(btn1)
    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! 💪\n"
    "Я — твой персональный бот-тренер, и моя цель — помочь тебе стать сильнее, красивее и круче! 🚀\n"
    "Всего пару вопросов — и я подберу для тебя программу тренировок, которая реально работает.\n"
    "Готов начать путь к новым результатам? 🔥",
        reply_markup = markup)

def on_click(message):
    if message.text == "Оценить фото":
        bot.send_message(message.chat.id, f'{message.from_user.first_name} отправь мне свое фото')
    elif message.text == "текст 2":
        bot.send_message(message.chat.id, 'Текст для кнопки 2')
    elif message.text == "текст 3":
        bot.send_message(message.chat.id, 'Текст для кнопки 3')

@bot.message_handler(content_types=['photo'])
def photo(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn2 = telebot.types.InlineKeyboardButton('Изменить текст', callback_data='edi')
    markup.row(btn1, btn2)
    bot.reply_to(message, "Неплохо:", reply_markup=markup)

def send_long_message(chat_id, text):
    """

    :rtype: None
    """
    max_length = 4000
    for i in range(0, len(text), max_length):
        bot.send_message(chat_id, text[i:i + max_length])

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edi':
        bot.edit_message_text('Новый текст', callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'bild':
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton('✅ Да', callback_data='spec_yes')
        btn2 = telebot.types.InlineKeyboardButton('❌ Нет', callback_data='spec_no')
        markup.row(btn1, btn2)
        bot.edit_message_text(
            "🏋️ Хочешь сделать упор на определенную группу мышц?\n(добавить специализацию)",
            callback.message.chat.id,
            callback.message.message_id,
            reply_markup=markup
        )

    elif callback.data == 'spec_yes':
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton('💪 Грудь', callback_data='chest_spec')
        btn2 = telebot.types.InlineKeyboardButton('🦍 Спина', callback_data='back_spec')
        btn3 = telebot.types.InlineKeyboardButton('🦵 Ноги', callback_data='legs_spec')
        btn4 = telebot.types.InlineKeyboardButton('⚡ Руки', callback_data='arms_spec')
        btn5 = telebot.types.InlineKeyboardButton('🏋️ Плечи', callback_data='shoulders_spec')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5)
        bot.edit_message_text(
            "Выбери мышечную группу для специализации:",
            callback.message.chat.id,
            callback.message.message_id,
            reply_markup=markup
        )
    elif callback.data == 'chest_spec':
        text = specialization_chest.get_chest_specialization()
        send_long_message(callback.message.chat.id, text)
        markup = telebot.types.InlineKeyboardMarkup()
        btn2 = telebot.types.InlineKeyboardButton('📋 Выбрать другую программу', callback_data='prog')
        markup.row(btn2)
        bot.send_message(
            callback.message.chat.id,
            "✅ Программа тренировок отправлена!",
            reply_markup=markup
        )

    elif callback.data == 'back_spec':
        text = specialization_back.get_back_specialization()
        send_long_message(callback.message.chat.id, text)
        markup = telebot.types.InlineKeyboardMarkup()
        btn2 = telebot.types.InlineKeyboardButton('📋 Выбрать другую программу', callback_data='prog')
        markup.row(btn2)
        bot.send_message(
            callback.message.chat.id,
            "✅ Программа тренировок отправлена!",
            reply_markup=markup
        )

    elif callback.data == 'legs_spec':
        text = specialization_legs.get_legs_specialization()
        send_long_message(callback.message.chat.id, text)
        markup = telebot.types.InlineKeyboardMarkup()
        btn2 = telebot.types.InlineKeyboardButton('📋 Выбрать другую программу', callback_data='prog')
        markup.row(btn2)
        bot.send_message(
            callback.message.chat.id,
            "✅ Программа тренировок отправлена!",
            reply_markup=markup
        )

    elif callback.data == 'arms_spec':
        text = specialization_arms.get_arms_specialization()
        send_long_message(callback.message.chat.id, text)
        markup = telebot.types.InlineKeyboardMarkup()
        btn2 = telebot.types.InlineKeyboardButton('📋 Выбрать другую программу', callback_data='prog')
        markup.row(btn2)
        bot.send_message(
            callback.message.chat.id,
            "✅ Программа тренировок отправлена!",
            reply_markup=markup
        )

    elif callback.data == 'shoulders_spec':
        text = specialization_shoulders.get_shoulders_specialization()  # функция для плеч
        send_long_message(callback.message.chat.id, text)
        markup = telebot.types.InlineKeyboardMarkup()
        btn2 = telebot.types.InlineKeyboardButton('📋 Выбрать другую программу', callback_data='prog')
        markup.row(btn2)
        bot.send_message(
            callback.message.chat.id,
            "✅ Программа тренировок отправлена!",
            reply_markup=markup
        )

    elif callback.data == 'spec_no':
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton('3 раза', callback_data='bb3')
        btn2 = telebot.types.InlineKeyboardButton('4 раза', callback_data='bb4')
        markup.row(btn1, btn2)
        bot.edit_message_text(
            "Сколько раз в неделю будешь тренироваться?",
            callback.message.chat.id,
            callback.message.message_id,
            reply_markup=markup
        )

    elif callback.data == 'bb3':
        text = body_3x.get_program()
        send_long_message(callback.message.chat.id, text)
        markup = telebot.types.InlineKeyboardMarkup()
        btn2 = telebot.types.InlineKeyboardButton('📋 Выбрать другую программу', callback_data='prog')
        markup.row(btn2)
        bot.send_message(
            callback.message.chat.id,
            "✅ Программа тренировок отправлена!",
            reply_markup=markup
        )
    elif callback.data == 'bb4':
        text = body_4x.get_program()
        send_long_message(callback.message.chat.id, text)
        markup = telebot.types.InlineKeyboardMarkup()
        btn2 = telebot.types.InlineKeyboardButton('📋 Выбрать другую программу', callback_data='prog')
        markup.row(btn2)
        bot.send_message(
            callback.message.chat.id,
            "✅ Программа тренировок отправлена!",
            reply_markup=markup
        )
    elif callback.data == 'prog':
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton('🏋️ Бодибилдинг', callback_data='bild')
        btn2 = telebot.types.InlineKeyboardButton('🦾 Жим лежа', callback_data='bench')
        markup.row(btn1, btn2)
        bot.edit_message_text(
            "💪 Выбери программу тренировок:",
            callback.message.chat.id,
            callback.message.message_id,
            reply_markup=markup
        )
    elif callback.data == 'option1':
        if callback.message.chat.id in user_pm:
            pm = user_pm[callback.message.chat.id]
            text = program.build_program(pm)
            bot.edit_message_text(text, callback.message.chat.id, callback.message.message_id)
            markup = telebot.types.InlineKeyboardMarkup()
            btn2 = telebot.types.InlineKeyboardButton('📋 Выбрать другую программу', callback_data='prog')
            markup.row(btn2)
            bot.send_message(
                callback.message.chat.id,
                "✅ Программа тренировок отправлена!",
                reply_markup=markup
            )
        else:
            bot.edit_message_text(
                "Сначала введи вес! 🏋️",
                callback.message.chat.id,
                callback.message.message_id
            )

    elif callback.data == 'option2':
        if callback.message.chat.id in user_pm:
            pm = user_pm[callback.message.chat.id]
            text = program.build_program2(pm)
            text2 = program.build_program3(pm)
            bot.delete_message(callback.message.chat.id, callback.message.message_id)
            send_long_message(callback.message.chat.id, text)
            send_long_message(callback.message.chat.id, text2)
            markup = telebot.types.InlineKeyboardMarkup()
            btn2 = telebot.types.InlineKeyboardButton('📋 Выбрать другую программу', callback_data='prog')
            markup.row(btn2)
            bot.send_message(
                callback.message.chat.id,
                "✅ Программа тренировок отправлена!",
                reply_markup=markup
            )
        else:
            bot.edit_message_text(
                "Сначала введи вес! 🏋️",
                callback.message.chat.id,
                callback.message.message_id
            )
    elif callback.data == 'bench':
        bot.edit_message_text("Сколько ты сейчас жмешь? 🏋️‍♂️\nВведи вес в килограммах, чтобы я мог подобрать программу под тебя.", callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['site', 'website'])
def site(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(
        text='Перейти на сайт',
        url='https://i.ytimg.com/vi/PqZ2VdOaT0U/maxresdefault.jpg?sqp=-oaymwEoCIAKENAF8quKqQMcGADwAQH4Ac4FgAKACooCDAgAEAEYZCBlKFAwDw==&amp;rs=AOn4CLCh2LuzIfZPn1pE_hHLbT3Ldyf3wA'
    )
    markup.add(button)
    bot.send_message(message.chat.id, "Нажми кнопку:", reply_markup=markup)

user_pm = {}
@bot.message_handler(content_types=['text'])
def info(message):
    text = message.text.lower().strip()
    if text == 'привет':
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!")
    elif text == 'id':
        bot.reply_to(message, f"ID: {message.from_user.id}")
    elif text.isdigit():
        num = int(text)
        if 1 < num < 400:
            user_pm[message.chat.id] = num
            markup = telebot.types.InlineKeyboardMarkup()
            btn1 = telebot.types.InlineKeyboardButton('2 раза', callback_data='option1')
            btn2 = telebot.types.InlineKeyboardButton('3 раза', callback_data='option2')
            markup.row(btn1, btn2)
            bot.reply_to(message, f"{message.from_user.first_name}, сколько раз в неделю планируешь жать? 💪\nВыбери вариант, чтобы я составил твою программу тренировок! 🏋️‍♂️", reply_markup=markup)



bot.polling(none_stop=True)