# Imports
import pygame
from pygame.locals import *
import sys

import graphics
import height_generation
import water


heightmap = height_generation.create_heightmap()


# Display loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    graphics.draw_noise(heightmap)

    if water.cleared != 0:
        water.clear_water(heightmap, 30)

    pygame.time.Clock().tick(1)
    pygame.display.update()
