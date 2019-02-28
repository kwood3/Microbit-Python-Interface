# Dice - Written by Koby W. For 'Python Interface' project w/ Moh Atieh

from microbit import *  # importing the 'microbit' module
import random           # importing the 'random' module
display.show('-')       # shows '-' on the display

while True:                                      # 'while' condition for when the microbit is on
    if accelerometer.was_gesture('shake'):       # 'accelerometer' is a class and 'was_gesture' is an attribute.
        display.clear()                          # clears the display    
        sleep(1000)                              # pauses program for 1000 ms
        display.show(str(random.randint(1, 6)))  # displays a random number from 1-6
    sleep(10)                                    # pauses for 10ms                    
