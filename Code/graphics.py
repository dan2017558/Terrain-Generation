import pygame
from pygame.locals import *

# Constants
PIXELS = [960, 720]
GRID_SIZE = [240, 180]

pygame.init()
pygame.display.set_caption("Terrain Generation")
Display = pygame.display.set_mode((PIXELS[0], PIXELS[1]))

def draw_noise(heightmap):
    for row in range(GRID_SIZE[1]):
        for column in range(GRID_SIZE[0]):
            height = heightmap[row][column]
            pygame.draw.rect(
                Display, 
                (height, height, height), 
                Rect(column * (PIXELS[0] / GRID_SIZE[0]), row * (PIXELS[1] / GRID_SIZE[1]), (PIXELS[0] / GRID_SIZE[0]), (PIXELS[1] / GRID_SIZE[1]))
            )