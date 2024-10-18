# Imports
import pygame
from pygame.locals import *
from perlin_noise import PerlinNoise
import sys

# Constants
PIXELS = 640
WIDTH = 640
OCTAVES = (4, 16, 64, 256)
COLOURS = {
    "DARK_BLUE": (0, 0, 170),
    "BLUE": (0, 0, 200),
    "LIGHT_BLUE": (50, 50, 255),
    "BEIGE": (255, 255, 0),
    "LIGHT_GREEN": (0, 240, 0),
    "GREEN": (0, 200, 0),
    "DARK_GREEN": (0, 160, 0),
    "GREY": (155, 155, 155),
    "WHITE": (255, 255, 255)
}

# Initialize pygame and set the display
pygame.init()
pygame.display.set_caption("Terrain Generation")
Display = pygame.display.set_mode((PIXELS, PIXELS))

# Create 4 noise layers by feeding set octaves into the PerlinNoise function
Noise_Layers = [PerlinNoise(octaves=o) for o in OCTAVES]

# 2d list with generated values between -1 & 1 exclusive
World = [[(sum(1/(o+1) * Noise_Layers[o]([row/WIDTH, column/WIDTH]) for o in range(len(Noise_Layers)))) for column in range(WIDTH)] for row in range(WIDTH)]

# Define height thresholds and corresponding colours
height_thresholds = [
    (0, "DARK_BLUE"),
    (8, "BLUE"),
    (10, "LIGHT_BLUE"),
    (15, "BEIGE"),
    (20, "LIGHT_GREEN"),
    (35, "GREEN"),
    (50, "DARK_GREEN"),
    (60, "GREY"),
]

# Maximum colour for heights above the last threshold
default_colour = COLOURS["WHITE"]

# Assign colours to world cell values
for row in range(WIDTH):
    for column in range(WIDTH):
        height = int(World[row][column] * 100)  # Integer with magnitude between 0-100 exlusive
        Colour = default_colour  # Start with the default colour

        for threshold, colour in height_thresholds:
            if height < threshold:
                Colour = COLOURS[colour]
                break
        pygame.draw.rect(Display, Colour, Rect(column * (PIXELS / WIDTH), row * (PIXELS / WIDTH), (PIXELS / WIDTH), (PIXELS / WIDTH)))

# Display loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    pygame.time.Clock().tick(1)
