from constants import TOKEN
from messages import HELLO,MOTIVATION, LOSE_WEIGHT1, LOSE_WEIGHT2,LS,ST1,ST2,NG1,NG2,SP1,SP2,LIVE1,LIVE2,LOVE1,LOVE2,LOVE3
from telebot import types
import messages
import database
import random
import telebot
import requests



bot = telebot.TeleBot(TOKEN)

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn2 = types.KeyboardButton('STUDY')
itembtn3 = types.KeyboardButton('LOSE WEIGHT')
itembtn4 = types.KeyboardButton('LIVE')
itembtn5 = types.KeyboardButton('SPORT')
itembtn6=types.KeyboardButton('NOT GIVE UP')
itembtn7=types.KeyboardButton('LOVE YOURSELF')
markup.row(itembtn2,itembtn3 )
markup.row(itembtn4,itembtn5 )
markup.row(itembtn6,itembtn7)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, messages.HELLO)
    bot.send_message(message.chat.id, ':)')
   


@bot.message_handler(commands=['motivation'])
def get_motivation(message):
   
    bot.reply_to(message, messages.MOTIVATION)
    print('inserted')
    bot.send_message(message.chat.id, "motivation to:",reply_markup=markup)
    

@bot.message_handler(commands=['photo'])
def send_photo(message):
    photo = open('images/sport/ph.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    #bot.send_message(message.chat.id, message.text)
    if message.text=="LOSE WEIGHT":
        bot.send_message(message.chat.id,random.choice([LOSE_WEIGHT1,LOSE_WEIGHT2,LS]))
        photo = open('images/loseweight/lw2.jpg', 'rb')
        photo2=open('images/loseweight/lw.jpg', 'rb')
        photo3=open('images/loseweight/lw3.jpg', 'rb')
        bot.send_photo(message.chat.id,random.choice([photo,photo2,photo3]))
    if message.text=="LIVE":
        bot.send_message(message.chat.id, random.choice([LIVE1,LIVE2]))
        photo = open('images/live/live.jpg', 'rb')
        photo2=open('images/live/l2.jpg', 'rb')
        bot.send_photo(message.chat.id,random.choice([photo,photo2]))

    if message.text=="STUDY":
        bot.send_message(message.chat.id, random.choice([ST1,ST2]))
        photo = open('images/study1.jpg', 'rb')
        photo1=open('images/study/stu.jpg','rb')
        photo2=open('images/study/stu2.jpg','rb')
        bot.send_photo(message.chat.id,random.choice([photo,photo2,photo1]))

    if message.text=="SPORT":
        bot.send_message(message.chat.id, random.choice([SP1,SP2]))
        photo = open('images/sport/sp2.jpg', 'rb')
        photo1=open('images/sport/sp.jpg','rb')
        bot.send_photo(message.chat.id,random.choice([photo,photo1]))

    if message.text=="NOT GIVE UP":
        bot.send_message(message.chat.id, random.choice([NG1,NG2]))
        photo = open('images/notgiveup/g.jpg', 'rb')
        bot.send_photo(message.chat.id,photo)        
    if message.text=="LOVE YOURSELF":
        bot.send_message(message.chat.id, random.choice([LOVE1,LOVE2,LOVE3]))
        photo = open('images/loveyourself/lv.jpg', 'rb')
        photo2=open('images/loveyourself/l.jpg', 'rb')
        photo3=open('images/loveyourself/love.jpg', 'rb')
        bot.send_photo(message.chat.id,random.choice([photo,photo2,photo3]))

if __name__ == '__main__':
    #запустим бесконечный цикл получения новых записей со стороны Telegram
    #Функция polling запускает т.н. Long Polling, 
    #а параметр none_stop=True говорит, что бот должен стараться не прекращать работу при возникновении каких-либо ошибок.
    print('Starting motivation BOT')
    bot.polling()
    