from machine import Pin
from time import sleep

button=Pin(5,Pin.IN)
led=Pin(4,Pin.OUT)

while True:
  led.value(button.value())
  

