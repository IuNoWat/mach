import rpi_ws281x as rpi
import time

meh = 15
total = 0.04
time_on = total*0.05
time_off = total*0.95
strip = rpi.PixelStrip(meh,10)

strip.begin()

while True :
    for i in range(0,meh) :
        strip.setPixelColor(i,rpi.Color(255,255,255))
    strip.show()
    time.sleep(time_on)
    for i in range(0,meh) :
        strip.setPixelColor(i,rpi.Color(0,0,0))
    strip.show()
    time.sleep(time_off)