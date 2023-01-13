'''import pygame
pygame.init()
pygame.mixer.music.load('mp3-tocando-musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('mp3-tocando-musica.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()