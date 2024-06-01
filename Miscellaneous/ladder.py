import pygame
from random import randint

time_clocks = pygame.time.Clock()

# Initialize
pygame.init()
width_screen = 1366
height_screen = 768

ic = pygame.image.load("resources/icon.png")
game_layout_display = pygame.display.set_mode((width_screen, height_screen), pygame.FULLSCREEN)
pygame.display.set_caption("Snakes and Ladders Game ")
pygame.display.set_icon(ic)
pygame.display.update()

# Graphics:
black_color = (10, 10, 10)