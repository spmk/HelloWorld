#!/usr/bin/python3

import telepot
import time
from telepot.loop import MessageLoop
import statusLEDs
import execute

def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']
	
	print('Got command: %s' % command)
	
	if command == '/status':
		bot.sendMessage(chat_id, "Alles gut :)")
	elif command == '/warpingLED':
		bot.sendMessage(chat_id, "Rote LED ist an!")
		statusLEDs.lightLed("warping")
	elif command == '/no_warpingLED':
		bot.sendMessage(chat_id, "Gruene LED ist aus!")
		statusLEDs.lightLed("no_warping")
		
bot = telepot.Bot('1405480476:AAHBt_66kwETu0BYK0Y4mtk07t4LtDEVa9c') #Token

MessageLoop(bot, handle).run_as_thread()
print("Hi! I am your personal warping assistant!")
bot.sendMessage("1405736760", "Hi I am your personal warping assistent!")
bot.sendMessage("1405736760", "I will text you if warping occurs.")

def sendMessage():
	bot.sendMessage("1405736760", "Warping erkannt und Drucker abgeschaltet!")
