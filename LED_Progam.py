'''Hello friends I am Aman Yadav.
This program only for initialization of a LED and turn it on.
you can watch video tutorial on youTube - www.youtube.com/martianiot for full course of "MicroPython Tutorial in hindi"
follow me on instagrame "amanyadav.io" to be updated with my all techPost :)
   '''

from machine import Pin  # Here I have imported Pin class from machine module.   
from time import sleep   # In this line I have imported sleep class form time module.

led=Pin(4,Pin.OUT)       # Here I have called Pin function, and what call function returns saved in a variable named led.
while True:              # here i have used while loop and put here True to make infinite loop.
  led.value(1)           # And here I have put 1 in led value to turn led on.
