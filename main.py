# to install library: pip3 install pyTelegramBotAPI
import random
import urllib
import json
import codecs
import re
import time

import telebot

token = codecs.open("holykey.txt", "r", "utf-8").read()
bot = telebot.TeleBot(token)

#logChatId = 'logChatId'

#randPhrases = codecs.open("ne_tupi_phrases.txt", "r", "utf-8").read().split("\n")
#randNeurals = codecs.open("ne_tupi_neurals.txt", "r", "utf-8").read().split("\n")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "бомжур пирожочки")
    #send_logs(message)


@bot.message_handler(commands=['getChatId'])
def send_katy(message):
    bot.send_message(message.chat.id, "такой: " + str(message.chat.id))
    #send_logs(message)


@bot.message_handler(commands=['ping'])
def perform_ping(message):
    bot.send_message(message.chat.id, "Себя попингуй")

'''@bot.message_handler(commands=['weather'])
def send_weather_nsu(message):
    bot.send_message(message.chat.id, 'TODO')
    send_logs(message)'''


@bot.message_handler(func=lambda message: True, content_types=['text'])
def huecho_msg(message):
    NON_LETTERS = re.compile('[^а-яё \-]+', flags=re.UNICODE)
    ONLY_DASHES = re.compile('^\-+$', flags=re.UNICODE)
    PREFIX = re.compile("^[бвгджзйклмнпрстфхцчшщьъ]+", flags=re.UNICODE)
    vowels = {'о', 'е', 'а', 'я', 'у', 'ю', 'ы'}
    rules = {'о': 'ё', 'а': 'я', 'у': 'ю', 'ы': 'и'}
    huendom = random.random()
    text_msg = message.text
    words = text_msg.split()
    user_name = message.from_user.username
    if user_name is None:
        user_name = message.from_user.first_name
    if str(text_msg).lower() == 'нет':
        bot.send_message(message.chat.id, user_name + ', пидора ответ')
    if huendom > 0.87:
        try:
            if len(words) < 3:
                pass
            word = NON_LETTERS.sub("", words[-1].lower())
            if ONLY_DASHES.match(word):
                pass
            postfix = PREFIX.sub("", word)
            if word[:2] == "ху" and postfix[1] in rules.values():
                pass
            if len(postfix) < 3:
                pass
            if postfix[0] in rules:
                if postfix[1] not in vowels:
                    huemessage = "ху%s%s" % (rules[postfix[0]], postfix[1:])
                else:
                    if postfix[1] in rules:
                        huemessage = u"ху%s%s" % (rules[postfix[1]], postfix[2:])
                    else:
                        huemessage = u'ху%s' % postfix[1:]
            else:
                huemessage = u"ху%s" % postfix
            bot.send_message(message.chat.id, user_name + ', ' + huemessage)
        except:
            pass
    if huendom < 0.01:
        bot.send_message(message.chat.id, 'го бухнём всем чатом')


'''@bot.message_handler(func=lambda message: True, content_types=['text'])
def send_logs(message):
    chat_id = str(message.chat.id)
    user_name = message.from_user.username
    if user_name is None:
        user_name = message.from_user.first_name + message.from_user.last_name
    message = message.text
    log = chat_id + " | " + user_name + " | " + message
    bot.send_message(logChatId, log)'''


def bot_launch():
    try:
        if __name__ == '__main__':
            bot.polling(none_stop=True, interval=0)
    except:
        time.sleep(60)
        bot_launch()

bot_launch()