'''Hello friends I am Aman Yadav.
This program only for initialization of a LED and turn it on.
you can watch video tutorial on youTube - www.youtube.com/martianiot for full course of "MicroPython Tutorial in hindi"
follow me on instagrame "amanyadav.io" to be updated with my all techPost :)
   '''

from machine import Pin    # Here I have imported Pin class from machine module.
from time import sleep     # In this line I have imported sleep class form time module.

        
led=Pin(4,Pin.OUT)        # LED Pin Initialization


while True:
      
  led.value(1)           # Turn On LED for half second
  sleep(0.5)

  led.value(0)          # Turn off LED for half second
  sleep(0.5)

