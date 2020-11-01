#Faca um programa em Python que abra e reproduza um audio em MP3
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('mario.mp3')
pygame.mixer_music.play(0)


pygame.event.wait()