#!/usr/bin/python3
from hx711 import HX711
import RPi.GPIO as GPIO
import statusLEDs
import Relais
import time
import telegrambot

if __name__ == "__main__": 
	try:
		GPIO.setmode(GPIO.BCM)
		hx711 = HX711(dout_pin=5,pd_sck_pin=6,
						gain_channel_A=64,select_channel='A')
		
		hx711.reset()   #Before we start, reset the HX711 (not obligate)
		hx711.zero()    #Offset eliminieren
		
		#Scale Ratio setzen
		scaleRatio = -1 #Spannungswert fuer Warping initial
		limit = 10000 #Wert, ab dem Warping erkannt wird
		averageOfXValues = 10 #Anzahl an Ausgelesenen Werten, die zur Auswertung gemittelt werden
		hx711.set_scale_ratio(scaleRatio)
		
		#Gewichte ausgeben, LEDs Relaise ansteuern
		print("Now, I will read data in infinite loop. To exit press 'CTRL + C'")
		input('Press Enter to begin reading')
		print('Current value measured is: ')
		while True:
			outputvalue = hx711.get_weight_mean(averageOfXValues)
			print(outputvalue, "") # "" steht für die Einheit
			if outputvalue>limit:
				statusLEDs.lightLed("warping")
				Relais.statusDrucker("warping")
				telegrambot.sendMessage()
				time.sleep(20)
				Relais.statusDrucker("no_warping")
				#userinput = input("Fehler erkannt! Druck Fortsetzen? (y / n)" ) #test
				#if userinput == "y":
					#Print("Strom wird wieder eingeschaltet. Druck kann manuell fortgesetzt werden.")
			#else:
				#statusLEDs.lightLed("no_warping")
			
	except (KeyboardInterrupt, SystemExit): #Programm kann mit Ctrl + C angehalten werden 
		print("Pfiat di Gott! :D")

	finally:
		GPIO.cleanup()

 
