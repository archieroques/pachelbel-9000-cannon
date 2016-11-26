#!/usr/bin/env python


'''This code is to trigger an all-singing all-dancing cannon when the code runs

It flashes 4 Pimoroni mote sticks rainbow colours, then shows a coundown from 8
on them

Then, it turns a Flotilla motor on, which was set up to pop a party popper
It also sticks a GPIO pin high, which I used to trigger a transistor. This
then triggers an automatic air freshner to squirt, which in turn produces gas
which ignites as it's sprayed over a candle. Juicy!

The code is dependant on my flotilla-easy library, and also the Pimoroni mote and
flotilla libraries. It's also dependent on the PrettyTable module, the time
module, and the RPi.GPIO module (as it was running on a Raspberry Pi (2)). 



import Flotilla
import time
from colorsys import hsv_to_rgb
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

from mote import Mote


mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

try:
    for i in range(500):
        h = time.time() * 50
        for channel in range(4):
            for pixel in range(16):
                hue = (h + (channel * 64) + (pixel * 4)) % 360
                r, g, b = [int(c * 255) for c in hsv_to_rgb(hue/360.0, 1.0, 1.0)]
                mote.set_pixel(channel + 1, pixel, r, g, b)
        mote.show()
        time.sleep(0.01)
    mote.clear()
    mote.show()
    for i in range(0, 15, 2):
        mote.set_pixel(1, i, 255, 255, 255)
        mote.set_pixel(2, i+1, 255, 255, 255)
        mote.set_pixel(3, i, 255, 255, 255)
        mote.set_pixel(4, i+1, 255, 255, 255)
        mote.show()
        time.sleep(1)
    Flotilla.motor(63)
    GPIO.output(2, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(2, GPIO.LOW)
        

except KeyboardInterrupt:
    mote.clear()
    mote.show()
    Flotilla.motor(0)
