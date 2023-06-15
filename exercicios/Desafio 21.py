import pygame
pygame.init()
L = input('musicas disponiveis: hardstyle ou linkpark ')
M = L
pygame.mixer_music.load('{}.mp3'.format(M))
pygame.mixer_music.play()
pygame.event.wait()
input('pressione enter para finalizar')


