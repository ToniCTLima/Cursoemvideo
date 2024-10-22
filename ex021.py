# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# Primeira tentativa com a solução do professor a música não tocava, coloquei o arquivo no CO-PILOT ele adicionou os comando pygame.mixer.music.set_volume(1.0), arquivo tocou por um segundo e parou, CO-PILOT sugeriu colocar o comando while pygame.mixer.music.get_busy():

import pygame
import time
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(1)
pygame.event.wait()


