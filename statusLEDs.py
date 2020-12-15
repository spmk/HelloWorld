#!/usr/bin/python3

from gpiozero import LED
from signal import pause

'''
Achtung unterschied PINs und GPIO
'''

green = LED("GPIO16")
red = LED("GPIO26")

def lightLed(status):
    if status == "warping":
        red.on()
        green.off()
    elif status == "no_warping":
        green.on()
        red.off()
    else:
        green.blink()
        red.blink()
        







