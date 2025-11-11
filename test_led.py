import rpi_ws281x as rpi
import time

meh = 144

strip = rpi.PixelStrip(meh,18)

strip.begin()

while True :
    for i in range(0,meh) :
        for j in range(0,meh) :
            strip.setPixelColor(j,rpi.Color(0,0,0))
        strip.setPixelColor(i,rpi.Color(255,255,255))
        strip.show()
        time.sleep(0.01)
    for i in range(0,meh) :
        for j in range(0,meh) :
            strip.setPixelColor(j,rpi.Color(0,0,0))
        strip.setPixelColor(meh-i,rpi.Color(255,255,255))
        strip.show()
        time.sleep(0.01)