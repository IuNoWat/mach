import pygame
import time

pygame.mixer.init(48000, -16, 1, 4096)

meh = pygame.mixer.music.load("/home/pi/Desktop/mach/music.mp3")

pygame.mixer.music.play()

time.sleep(100)

pygame.mixer.music.stop()