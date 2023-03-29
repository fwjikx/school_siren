import telebot
from telebot import types
from mainToken import tg_token

bot = telebot.TeleBot('6218815330:AAErc23v-2MUKRBVgeBwKb70XPVSb6IJhqo')
chat_id = tg_token


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здравствуйте, <b>{message.from_user.first_name}</b> Я бот, который может:' \
           f'\n <b>-предоставить информацию об огранизции \n' \
           f' -предоставить расписание \n -предосавить информацию о преподавателях \n' \
           f' -предоставить список направлений \n -предоставить контактные данные \n' \
           f' -записать ребенка</b>\n' \
           f' Просто напишите, о чем вы хотите узнать'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    mess = f'Я бот, который может:\n <b>-предоставить информацию об организции \n' \
           f' -предоставить расписание \n -предосавить информацию о преподавателях \n' \
           f' -предоставить список направлений \n -предоставить контактные данные \n' \
           f' -записать ребенка</b>\n' \
           f' Просто напишите, о чем вы хотите узнать'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if 'рганиз' in message.text.lower() or 'орг' in message.text.lower():
        bot.send_message(message.chat.id,
                         'ЦЦОД "IT-Куб" Вурнарского сельскохозяйственного техникума Минобразования Чувашии.\n'
                         '«IT-куб»— федеральная сеть центров цифрового образования.\n'
                         '«IT-куб»— новая современная площадка дополнительного образования и '
                         'интеллектуального развития детей и подростков в сфере современных '
                         'информационных и телекоммуникационных технологий.\n«IT-куб» — это уникальная атмосфера для '
                         'технического творчества, где дети и подростки не просто изучают информационные технологии, '
                         'а создают программные проекты.', parse_mode='html')

    elif 'асписан' in message.text:
        p1 = open('rasp1.jpg', 'rb')
        p2 = open('rasp2.jpg', 'rb')
        p3 = open('rasp3.jpg', 'rb')
        p4 = open('rasp4.jpg', 'rb')
        p5 = open('rasp5.jpg', 'rb')
        bot.send_photo(message.chat.id, p1, parse_mode='html')
        bot.send_photo(message.chat.id, p2, parse_mode='html')
        bot.send_photo(message.chat.id, p3, parse_mode='html')
        bot.send_photo(message.chat.id, p4, parse_mode='html')
        bot.send_photo(message.chat.id, p5, parse_mode='html')

    elif 'репод' in message.text.lower() or 'чител' in message.text.lower() or 'глава' in message.text.lower():
        bot.send_message(message.chat.id, '<b>Заместитель руководителя по работе с федеральной сетью и внешними партнерами</b>'
                                          ' - Петриченко Петр Александрович\n'
                                          '<b>Заместитель руководителя, заведующая учебной частью</b> - Казенова Ирина '
                                          'Петровна\n'
                                          '<b>Методист</b> - Мнейкина Анастасия Александровна\n'
                                          '<b>Педагог дополнительного образования</b> - Павлова Екатерина Сергеевна\n'
                                          '<b>Педагог дополнительного образования</b> - Репин Анатолий Владимирович\n'
                                          '<b>Педагог дополнительного образования</b> - Нарышкин Владимир Александрович\n'
                                          '<b>Педагог дополнительного образования</b> - Васильева Юлия Александровна\n'
                                          '<b>Педагог дополнительного образования</b> - Трофимова Кристина Сергеевна\n'
                                          '<b>Педагог дополнительного образования</b> - Никитин Александр Николаевич\n'
                                          '<b>Педагог дополнительного образования</b> - Иванов Руслан Олегович\n'
                                          '<b>Педагог дополнительного образования</b> - Глухов Владимир Анатольевич\n'
                                          '<b>Педагог дополнительного образования</b> - Чермаков Владимир Сергеевич\n'
                                          '<b>Педагог дополнительного образования</b> - Иванова Любовь Анатольевна', parse_mode='html')

    elif 'направ' in message.text.lower() or 'писок' in message.text.lower():
        bot.send_message(message.chat.id, '-Программирование на Python.\n'
                                          '-Разработка VR/AR -приложений.\n'
                                          '-Системное администрирование.\n'
                                          '-Основы программирования на Java.\n'
                                          '-Лаборатория программирования роботов.\n'
                                          '-Цифровая гигиена и работа с большими данными.\n'
                                          '-Основы алгоритмики. Пиктомир..\n'
                                          '-Шахматы.\n'
                                          '-Мобильная разработка.\n'
                                          '-Программирование на Scratch', parse_mode='html')

    elif 'контакт' in message.text.lower() or 'данные' in message.text.lower():
        bot.send_message(message.chat.id, 'Номер телефона: +7 (991) 465-11-55\n'
                                          'Сайт It-Cube: itcube21.ru', parse_mode='html')

    elif 'рив' in message.text.lower() or 'драв' in message.text.lower() or 'аров' in message.text or 'ку' in message.text.lower():
        bot.send_message(message.chat.id,
                         f'Здравствуйте, <b>{message.from_user.first_name}</b>. Я бот-помощник ЦЦОД it-куб.Вурнары.'
                         f'\nДля того, чтобы узнать мои возможности напишите /help',
                         parse_mode='html')

    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')

    elif 'ребен' in message.text.lower() or 'аписать ребен' in message.text.lower() or 'запись' in message.text.lower():
        bot.send_message(message.chat.id, 'Воспользуйтесь этим номером: +7 (991) 465-11-55\n'
                                          'Также можете написать в группу вк It-Cube: vk.com/public198282945', parse_mode='html')

    else:
        bot.send_message(message.chat.id, 'Извините, я вас не понимаю. \nОбратитесь к команде /help. ')


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(chat_id=chat_id, text=message.text)


bot.polling(none_stop=True)
