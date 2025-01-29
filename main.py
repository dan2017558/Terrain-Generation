# Imports
import pygame
from pygame.locals import *
from perlin_noise import PerlinNoise
import sys

# Constants
PIXELS = 800
GRID_SIZE = 800
#DEFAULT_FREQUENCY = 4
#PERSISTANCE = 0.5
#LACUNARITY = 2
#OCTAVES = 4

# Initialize pygame and set the display
pygame.init()
pygame.display.set_caption("Terrain Generation")
Display = pygame.display.set_mode((PIXELS, PIXELS))
noise_grid = []


def create_noise(PERSISTANCE, LACUNARITY, DEFAULT_FREQUENCY, OCTAVES):

    # Create Octave and frequencies
    octave_frequencies = (DEFAULT_FREQUENCY*LACUNARITY**OCTAVE for OCTAVE in range(OCTAVES))

    # Create Perlin noise layers
    noise_layers = [PerlinNoise(octaves=frequency) for frequency in octave_frequencies]

    # Generate grid of noise values
    for grid_row in range(GRID_SIZE):
        row_values = []
        for grid_col in range(GRID_SIZE): 
            combined_noise = 0  # Start with 0 as base avlue
            
            # Combine noise from all octaves (layers) into a single value
            for layer_index in range(len(noise_layers)):

                amplitude = 1 * PERSISTANCE**(layer_index)
                frequency_contribution = noise_layers[layer_index](
                    [grid_row / GRID_SIZE, grid_col / GRID_SIZE]
                )
                
                combined_noise += amplitude * frequency_contribution
            
            row_values.append(combined_noise)

        noise_grid.append(row_values)


def draw_noise(noise_grid):
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            height = int(abs(noise_grid[row][column]) * 100)
            pygame.draw.rect(Display, (height, height, height), Rect(column * (PIXELS / GRID_SIZE), row * (PIXELS / GRID_SIZE), (PIXELS / GRID_SIZE), (PIXELS / GRID_SIZE)))


# Create
settings = str(input("Settings: ")).split()
create_noise(float(settings[0]), float(settings[1]), float(settings[2]), int(settings[3]))

# Display loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    draw_noise(noise_grid)

    pygame.display.update()
    pygame.time.Clock().tick(1)
