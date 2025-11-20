from machine import Pin
import time

led = Pin(15, Pin.OUT)

button = Pin(14, Pin.IN, Pin.PULL_UP)

can_blink = True

while True:
    if button.value() == 0 and can_blink == True:
        for i in range(0, 2):
            led.value(1)
            time.sleep(0.1)
            led.value(0)
            time.sleep(0.1)
        can_blink = False
    else:
        led.value(0)
        if button.value() == 1 and can_blink == False:
            can_blink = True