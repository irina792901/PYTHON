from random import shuffle, randint

# CANDIES = 2021
CANDIES = 121
CANDIES_LIMIT = 28


def bot_run(candies: int) -> int:
    result = candies % 29
    if not result:
        result = randint(1, 28)
    return result


def moves(pl_act):
    first, second = players
    return second if pl_act == first else first


players = ["human", 'bot' if int(input('Play with bot 1 - yes, 0 - no? ')) else 'person']
shuffle(players)

active_player = players[0]
print(f'1 player - {players[0]}, 2 player - {players[1]}')

while CANDIES > 0:
    print(f'\nThere are {CANDIES} sweets on the table, you can take [1 .. {CANDIES_LIMIT}]')
    print(f"Player {active_player}'s move")

    if active_player == "bot":
        get_candies = bot_run(CANDIES)
        print(f'The bot took {get_candies} candies')
    else:
        get_candies = int(input(f'How many candies do you want {active_player}: '))

    # проверки
    if get_candies not in range(1, CANDIES_LIMIT + 1):
        print('Wrong move!')
    else:
        CANDIES -= get_candies
        if CANDIES > 0:
            active_player = moves(active_player)
        else:
            print(f'The player {active_player} won!')






Andrii Banduliak, [21.10.2022 1:21]
from email import message
import logging
from secrets import choice
from toke import *
#from na import *
from random import randint as r
from random import shuffle as sh


from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(name)

# Определяем константы этапов разговора
CANDIES = 120
CANDISE_LIM = 28



# функция обратного вызова точки входа в разговор
def start(update, _):
    
    update.message.reply_text(
        "Привет, это игра про конфеты,let's play" )
    update.message.reply_text('1 - bot\n, 2 - human\n, 3 - exit\n')
        # переходим к этапу GENDER, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список 
    # обработчиков, определенных в виде значения ключа GENDER
    return CHOISE

# Обрабатываем пол пользователя
def choice(update, _):
    global players, active_player
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал пол пользователя
    logger.info(user.first_name, update.message.text)
    # Следующее сообщение с удалением клавиатуры ReplyKeyboardRemove
    user_choise =update.message.text
    if user_choise in "1 2 3":
        if user_choise in "1 2":
            players = ["human", 'bot' if user_choise < '2' else 'person']
            sh(players)
            active_player = players[0]
        elif user_choise == "3":
            update.message.reply_text('good bye :)')
            return ConversationHandler.END
    else:
        update.message.reply_text("try again please: '1 - bot\n, 2 - human\n, 3 - exit\n'") 
        

# Обрабатываем фотографию пользователя
def photo(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем фото 
    photo_file = update.message.photo[-1].get_file()
    # скачиваем фото 
    photo_file.download(f'{user.first_name}_photo.jpg')
    # Пишем в журнал сведения о фото
    logger.info("Фотография %s: %s", user.first_name, f'{user.first_name}_photo.jpg')
    # Отвечаем на сообщение с фото
    update.message.reply_text(
        'Великолепно! А теперь пришли мне свое'
        ' местоположение, или /skip если параноик..'
    )
    # переходим к этапу LOCATION
    return LOCATION

# Обрабатываем команду /skip для фото
def skip_photo(update, _):
    # определяем пользователя
    user = update.message.from_user

Andrii Banduliak, [21.10.2022 1:21]
# Пишем в журнал сведения о фото
    logger.info("Пользователь %s не отправил фото.", user.first_name)
    # Отвечаем на сообщение с пропущенной фотографией
    update.message.reply_text(
        'Держу пари, ты выглядишь великолепно! А теперь пришлите мне'
        ' свое местоположение, или /skip если параноик.'
    )
    # переходим к этапу LOCATION
    return LOCATION

# Обрабатываем местоположение пользователя
def location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем местоположение пользователя
    user_location = update.message.location
    # Пишем в журнал сведения о местоположении
    logger.info(
        "Местоположение %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)
    # Отвечаем на сообщение с местоположением
    update.message.reply_text(
        'Может быть, я смогу как-нибудь навестить тебя!' 
        ' Расскажи мне что-нибудь о себе...'
    )
    # переходим к этапу BIO
    return BIO

# Обрабатываем команду /skip для местоположения
def skip_location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о местоположении
    logger.info("User %s did not send a location.", user.first_name)
    # Отвечаем на сообщение с пропущенным местоположением
    update.message.reply_text(
        'Точно параноик! Ну ладно, тогда расскажи мне что-нибудь о себе...'
    )
    # переходим к этапу BIO
    return BIO

# Обрабатываем сообщение с рассказом/биографией пользователя
def bio(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал биографию или рассказ пользователя
    logger.info("Пользователь %s рассказал: %s", user.first_name, update.message.text)
    # Отвечаем на то что пользователь рассказал.
    update.message.reply_text('Спасибо! Надеюсь, когда-нибудь снова сможем поговорить.')
    # Заканчиваем разговор.
    return ConversationHandler.END

# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END


if name == 'main':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров ConversationHandler 
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CHOISE: [MessageHandler(Filters.text, choice)],
            
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров conv_handler
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()


app = ApplicationBuilder().token("TOKEN").build()



От Aleksei всем 01:34 AM
bot = telebot.TeleBot(token)

Andrii Banduliak, [21.10.2022 1:21]
from email import message
import logging
from secrets import choice
from toke import *
#from na import *
from random import randint as r
from random import shuffle as sh


from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(name)

# Определяем константы этапов разговора
CANDIES = 120
CANDISE_LIM = 28



# функция обратного вызова точки входа в разговор
def start(update, _):
    
    update.message.reply_text(
        "Привет, это игра про конфеты,let's play" )
    update.message.reply_text('1 - bot\n, 2 - human\n, 3 - exit\n')
        # переходим к этапу GENDER, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список 
    # обработчиков, определенных в виде значения ключа GENDER
    return CHOISE

# Обрабатываем пол пользователя
def choice(update, _):
    global players, active_player
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал пол пользователя
    logger.info(user.first_name, update.message.text)
    # Следующее сообщение с удалением клавиатуры ReplyKeyboardRemove
    user_choise =update.message.text
    if user_choise in "1 2 3":
        if user_choise in "1 2":
            players = ["human", 'bot' if user_choise < '2' else 'person']
            sh(players)
            active_player = players[0]
        elif user_choise == "3":
            update.message.reply_text('good bye :)')
            return ConversationHandler.END
    else:
        update.message.reply_text("try again please: '1 - bot\n, 2 - human\n, 3 - exit\n'") 
        

# Обрабатываем фотографию пользователя
def photo(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем фото 
    photo_file = update.message.photo[-1].get_file()
    # скачиваем фото 
    photo_file.download(f'{user.first_name}_photo.jpg')
    # Пишем в журнал сведения о фото
    logger.info("Фотография %s: %s", user.first_name, f'{user.first_name}_photo.jpg')
    # Отвечаем на сообщение с фото
    update.message.reply_text(
        'Великолепно! А теперь пришли мне свое'
        ' местоположение, или /skip если параноик..'
    )
    # переходим к этапу LOCATION
    return LOCATION

# Обрабатываем команду /skip для фото
def skip_photo(update, _):
    # определяем пользователя
    user = update.message.from_user

Andrii Banduliak, [21.10.2022 1:21]
# Пишем в журнал сведения о фото
    logger.info("Пользователь %s не отправил фото.", user.first_name)
    # Отвечаем на сообщение с пропущенной фотографией
    update.message.reply_text(
        'Держу пари, ты выглядишь великолепно! А теперь пришлите мне'
        ' свое местоположение, или /skip если параноик.'
    )
    # переходим к этапу LOCATION
    return LOCATION

# Обрабатываем местоположение пользователя
def location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем местоположение пользователя
    user_location = update.message.location
    # Пишем в журнал сведения о местоположении
    logger.info(
        "Местоположение %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)
    # Отвечаем на сообщение с местоположением
    update.message.reply_text(
        'Может быть, я смогу как-нибудь навестить тебя!' 
        ' Расскажи мне что-нибудь о себе...'
    )
    # переходим к этапу BIO
    return BIO

# Обрабатываем команду /skip для местоположения
def skip_location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о местоположении
    logger.info("User %s did not send a location.", user.first_name)
    # Отвечаем на сообщение с пропущенным местоположением
    update.message.reply_text(
        'Точно параноик! Ну ладно, тогда расскажи мне что-нибудь о себе...'
    )
    # переходим к этапу BIO
    return BIO

# Обрабатываем сообщение с рассказом/биографией пользователя
def bio(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал биографию или рассказ пользователя
    logger.info("Пользователь %s рассказал: %s", user.first_name, update.message.text)
    # Отвечаем на то что пользователь рассказал.
    update.message.reply_text('Спасибо! Надеюсь, когда-нибудь снова сможем поговорить.')
    # Заканчиваем разговор.
    return ConversationHandler.END

# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END


if name == 'main':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров ConversationHandler 
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CHOISE: [MessageHandler(Filters.text, choice)],
            
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров conv_handler
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

Andrii Banduliak, [21.10.2022 1:41]
ImportError: cannot import name 'Filters' from 'telegram.ext' (C:\Users\andrj\AppData\Local\Programs\Python\Python310\lib\site-packages\telegram\ext\__init__.py)
pip install python-telegram-bot==13.14 -U
pip install python-telegram-bot==13.14 -U




















Andrii Banduliak, [21.10.2022 1:21]
# Пишем в журнал сведения о фото
    logger.info("Пользователь %s не отправил фото.", user.first_name)
    # Отвечаем на сообщение с пропущенной фотографией
    update.message.reply_text(
        'Держу пари, ты выглядишь великолепно! А теперь пришлите мне'
        ' свое местоположение, или /skip если параноик.'
    )
    # переходим к этапу LOCATION
    return LOCATION

# Обрабатываем местоположение пользователя
def location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем местоположение пользователя
    user_location = update.message.location
    # Пишем в журнал сведения о местоположении
    logger.info(
        "Местоположение %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)
    # Отвечаем на сообщение с местоположением
    update.message.reply_text(
        'Может быть, я смогу как-нибудь навестить тебя!' 
        ' Расскажи мне что-нибудь о себе...'
    )
    # переходим к этапу BIO
    return BIO

# Обрабатываем команду /skip для местоположения
def skip_location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о местоположении
    logger.info("User %s did not send a location.", user.first_name)
    # Отвечаем на сообщение с пропущенным местоположением
    update.message.reply_text(
        'Точно параноик! Ну ладно, тогда расскажи мне что-нибудь о себе...'
    )
    # переходим к этапу BIO
    return BIO

# Обрабатываем сообщение с рассказом/биографией пользователя
def bio(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал биографию или рассказ пользователя
    logger.info("Пользователь %s рассказал: %s", user.first_name, update.message.text)
    # Отвечаем на то что пользователь рассказал.
    update.message.reply_text('Спасибо! Надеюсь, когда-нибудь снова сможем поговорить.')
    # Заканчиваем разговор.
    return ConversationHandler.END

# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END


if name == 'main':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров ConversationHandler 
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CHOISE: [MessageHandler(Filters.text, choice)],
            
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров conv_handler
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

Andrii Banduliak, [21.10.2022 1:41]
ImportError: cannot import name 'Filters' from 'telegram.ext' (C:\Users\andrj\AppData\Local\Programs\Python\Python310\lib\site-packages\telegram\ext\__init__.py)

Andrii Banduliak, [21.10.2022 2:00]
from email import message
import logging
from secrets import choice
from toke import *
#from na import *
from random import randint as r
from random import shuffle as sh


from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(name)

# Определяем константы этапов разговора
CANDIES = 120
CANDISE_LIM = 28
CHOICE = 0


# функция обратного вызова точки входа в разговор
def start(update, _):

    update.message.reply_text(
        "Привет, это игра про конфеты,let's play")
    update.message.reply_text('1 - bot\n, 2 - human\n, 3 - exit\n')
    # переходим к этапу GENDER, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список
    # обработчиков, определенных в виде значения ключа GENDER
    return CHOICE

# Обрабатываем пол пользователя


def choice(update, _):
    global players, active_player
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал пол пользователя
    logger.info(user.first_name, update.message.text)
    # Следующее сообщение с удалением клавиатуры ReplyKeyboardRemove
    user_choise = update.message.text
    if user_choise in "1 2 3":
        if user_choise in "1 2":
            players = ["human", 'bot' if user_choise < '2' else 'person']
            sh(players)
            active_player = players[0]
        elif user_choise == "3":
            update.message.reply_text('good bye :)')
            return ConversationHandler.END
    else:
        update.message.reply_text(
            "try again please: '1 - bot\n, 2 - human\n, 3 - exit\n'")


# Обрабатываем фотографию пользователя
def photo(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем фото
    photo_file = update.message.photo[-1].get_file()
    # скачиваем фото
    photo_file.download(f'{user.first_name}_photo.jpg')
    # Пишем в журнал сведения о фото
    logger.info("Фотография %s: %s", user.first_name,
                f'{user.first_name}_photo.jpg')
    # Отвечаем на сообщение с фото
    update.message.reply_text(
        'Великолепно! А теперь пришли мне свое'
        ' местоположение, или /skip если параноик..'
    )
    # переходим к этапу LOCATION
    return LOCATION

Andrii Banduliak, [21.10.2022 2:00]
def skip_photo(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о фото
    logger.info("Пользователь %s не отправил фото.", user.first_name)
    # Отвечаем на сообщение с пропущенной фотографией
    update.message.reply_text(
        'Держу пари, ты выглядишь великолепно! А теперь пришлите мне'
        ' свое местоположение, или /skip если параноик.'
    )
    # переходим к этапу LOCATION
    return LOCATION

# Обрабатываем местоположение пользователя


def location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем местоположение пользователя
    user_location = update.message.location
    # Пишем в журнал сведения о местоположении
    logger.info(
        "Местоположение %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)
    # Отвечаем на сообщение с местоположением
    update.message.reply_text(
        'Может быть, я смогу как-нибудь навестить тебя!'
        ' Расскажи мне что-нибудь о себе...'
    )
    # переходим к этапу BIO
    return BIO

# Обрабатываем команду /skip для местоположения


def skip_location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о местоположении
    logger.info("User %s did not send a location.", user.first_name)
    # Отвечаем на сообщение с пропущенным местоположением
    update.message.reply_text(
        'Точно параноик! Ну ладно, тогда расскажи мне что-нибудь о себе...'
    )
    # переходим к этапу BIO
    return BIO

# Обрабатываем сообщение с рассказом/биографией пользователя


def bio(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал биографию или рассказ пользователя
    logger.info("Пользователь %s рассказал: %s",
                user.first_name, update.message.text)
    # Отвечаем на то что пользователь рассказал.
    update.message.reply_text(
        'Спасибо! Надеюсь, когда-нибудь снова сможем поговорить.')
    # Заканчиваем разговор.
    return ConversationHandler.END

# Обрабатываем команду /cancel если пользователь отменил разговор


def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.',
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END


if name == 'main':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater("5619410927:AAHJURUKGTcKqFOzCK3ilBCK_o3Fe7cd7Tw")
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров ConversationHandler
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CHOICE: [MessageHandler(Filters.text, choice)],

        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров conv_handler
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

