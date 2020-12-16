#!/usr/bin/python3
import telepot
import time
from telepot.loop import MessageLoop
import statusLEDs
import execute

#Hier sind alle Befehle definiert, die der Bot ausfuehren kann.
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
	elif command == '\help':
		bot.sendMessage(chat_id, "\status  -  Sendet ob Warping erkannt wurde oder nicht \n \warpingLED  -  Sendet welche LED an ist \n \no_warpingLED  -  Sendet Status der gruenen LED")
		

#Bot Objekt wird erstellt und diesem werden die Befehle uebergeben
bot = telepot.Bot('1405480476:AAHBt_66kwETu0BYK0Y4mtk07t4LtDEVa9c') #Token
MessageLoop(bot, handle).run_as_thread()

#Boot up Nachricht des Bots:
print("Hi! I am your personal warping assistant!") #Auf der Konsole
bot.sendMessage("1405736760", "Hi I am your personal warping assistent!") #In Telegram
bot.sendMessage("1405736760", "I will text you if warping occurs.") #In Telegram

#Diese Methode wird in execute.py aufgerufen, wenn Warping auftritt. 
def sendMessage():
	bot.sendMessage("1405736760", "Warping erkannt und Drucker abgeschaltet!")
