# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
import time
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(1)
pygame.event.wait()


