'''Hello friends I am Aman Yadav.
This program only for initialization of a LED and turn it on.
you can watch video tutorial on youTube - www.youtube.com/martianiot for full course of "MicroPython Tutorial in hindi"
follow me on instagrame "amanyadav.io" to be updated with my all techPost :)
   '''

from machine import Pin    # Here I have imported Pin class from machine module.
from time import sleep     # In this line I have imported sleep class form time module.

Red_LED=Pin(14,Pin.OUT)          # Initialization of Red_LED
Green_LED=Pin(12,Pin.OUT)        # Initialization of Green_LED
Yellow_LED=Pin(4,Pin.OUT)        # Initialization of Yellow_LED

Red_LED.value(0)                 # Make low all pins where leds are connected 
Green_LED.value(0)
Yellow_LED.value(0)

while True:
  Red_LED.value(1)               # Turn On Each LEDs after 0.5 second
  Green_LED.value(0)
  Yellow_LED.value(0)
  sleep(0.5)
  
  Red_LED.value(0)
  Green_LED.value(1)
  Yellow_LED.value(0)
  sleep(0.5)
  
  Red_LED.value(0)
  Green_LED.value(0)
  Yellow_LED.value(1)
  sleep(0.5)
  
  
