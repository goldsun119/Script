#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

import noti


def replyAptData(direction, user, highway):
    print(user, direction, highway)
    res_list = noti.getData( highway, direction )
    msg = ''
    for r in res_list:
        print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1>noti.MAX_MSG_LENGTH:
            noti.sendMessage( user, msg )
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        noti.sendMessage( user, msg )
    else:
        noti.sendMessage( user, '%s 방향에 해당하는 데이터가 없습니다.'%direction )


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')
    args2 = text.split(' ')

    if text.startswith('조회') and len(args)>1:
        print('try to 조회', args[1], args2[1])
        replyAptData( args2[1], chat_id, args[1] )
    else:
        noti.sendMessage(chat_id, '모르는 명령어입니다.\n조회 [고속도로명] [방향]을 입력하세요.')


today = date.today()
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', noti.TOKEN )

bot = telepot.Bot(noti.TOKEN)
pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...')

while 1:
  time.sleep(10)