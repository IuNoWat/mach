import pygame
import librosa
import numpy
import rpi_ws281x as rpi
import time
import os

print("Analysing Audio")

y, sr = librosa.load("/home/pi/Desktop/mach/music.mp3")

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print(f"Estimated tempo: {tempo} beats per minute")

# 4. Convert the frame indices of beat events into timestamps

beat_times = librosa.frames_to_time(beat_frames, sr=sr)

print(beat_times)

parts = [
    [9.42,rpi.Color(0,0,0)],
    [17.5,rpi.Color(50,50,50)],
    [25,rpi.Color(255,255,255)],
    [1000,rpi.Color(255,0,0)],
]

print(beat_times[0])

meh = 10
strip = rpi.PixelStrip(meh,10)
strip.begin()

def led_on() :
    for i in range(0,meh) :
        strip.setPixelColor(i,rpi.Color(255,255,255))
    strip.show()

def led_off() :
    for i in range(0,meh) :
        strip.setPixelColor(i,rpi.Color(0,0,0))
    strip.show()

#Play song

on = True
CLOCK= pygame.time.Clock()
FPS = 60
time_elapsed = 0

print("launching main loop")

led_on()
time.sleep(3)
led_off()

#os.system("/home/pi/Desktop/mach_env/bin/python /home/pi/Desktop/mach/sound.py")

pygame.mixer.init()

pygame.mixer.music.load("/home/pi/Desktop/mach/music.mp3")

pygame.mixer.music.play()

while on :
    print(beat_times[0])
    time_elapsed+=CLOCK.get_time()/1000
    if time_elapsed>beat_times[0] :
        led_on()
        beat_times = numpy.delete(beat_times,0)
    else :
        led_off()

    CLOCK.tick(FPS)

print(time_elapsed)