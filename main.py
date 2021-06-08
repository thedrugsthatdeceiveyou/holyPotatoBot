# to install library: pip3 install pyTelegramBotAPI
import random
import urllib
import json
import codecs
import re
import time
import os
import telebot

token = codecs.open("holykey.txt", "r", "utf-8").read()
bot = telebot.TeleBot(token)
randPhrases = codecs.open("holyPhrases.txt", "r", "utf-8").read()

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

@bot.message_handler(commands=['shrug'])
def perform_ping(message):
    bot.send_message(message.chat.id, "¯\_(ツ)_/¯")

def huecho_msg(message):
    NON_LETTERS = re.compile('[^а-яё \-]+', flags=re.UNICODE)
    ONLY_DASHES = re.compile('^\-+$', flags=re.UNICODE)
    PREFIX = re.compile("^[бвгджзйклмнпрстфхцчшщьъ]+", flags=re.UNICODE)
    vowels = {'о', 'е', 'а', 'я', 'у', 'ю', 'ы'}
    rules = {'о': 'ё', 'а': 'я', 'у': 'ю', 'ы': 'и'}
    text_msg = message.text
    words = text_msg.split()
    user_name = message.from_user.first_name
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
    except:
        pass

@bot.message_handler(func=lambda message: True, content_types=['text'])
def randomTalks(message):
    huendom = random.random()
    text_msg = message.text
    user_name = message.from_user.first_name
    if huendom > 0.09:
        huecho_msg(message)
    if huendom < 0.00001:
        bot.send_message(message.chat.id, 'го бухнём всем чатом')
    '''if 0.3 < huendom < 0.35:
        send_pict()'''
    if 'нет' in str(text_msg).lower():
        if 0.31 < huendom < 0.315:
            bot.send_message(message.chat.id, user_name + ', пидора ответ')
    if 'кто' in str(text_msg):
        if 0 < huendom < 0.3:
            bot.send_message(message.chat.id, '{}, мамка твоя'.format(user_name))


@bot.message_handler(func=lambda message: True, content_types=['text'])
def phrasesMsg(message):
    phrRandom = random.random()
    user_name = message.from_user.first_name
    if 0.2 < phrRandom < 0.7:
        bot.send_message(message.chat.id, random.choice(randPhrases).format(user_name))


def bot_launch():
    try:
        if __name__ == '__main__':
            bot.polling(none_stop=True, interval=0)
    except:
        time.sleep(60)
        bot_launch()

bot_launch()