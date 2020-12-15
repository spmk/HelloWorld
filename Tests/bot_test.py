import time
import random
import datetime
import telepot as tp
from telepot.loop import MessageLoop

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)
        
    if command == '/roll':
        bot.sendMessage(chat_id, chat_id)
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
        
#def sendMessage(msg):
    
def send(msg):
    bot = tp.Bot('1405480476:AAHBt_66kwETu0BYK0Y4mtk07t4LtDEVa9c')
    bot.sendMessage(chat_id="-140573676", text=msg)
    
#bot = tp.Bot('1453220620:AAFYArnMzhhIVvtg2yn8_r0i-ag3iVpPmR0')
bot = tp.Bot('1405480476:AAHBt_66kwETu0BYK0Y4mtk07t4LtDEVa9c')
bot.sendMessage('1405736760', "hi")

MessageLoop(bot, handle).run_as_thread()
print ("I am listening ...")


time.sleep(1)
