from perlin_noise import PerlinNoise
import graphics

# Constants
PERSISTANCE = 0.7
LACUNARITY = 2.5
DEFAULT_FREQUENCY = 1
OCTAVES = 6


def create_heightmap():
    heightmap = []
    avg_alt = 0
    # Create Octave and frequencies
    octave_frequencies = (DEFAULT_FREQUENCY*LACUNARITY**OCTAVE for OCTAVE in range(OCTAVES))

    # Create Perlin noise layers
    noise_layers = [PerlinNoise(octaves=frequency) for frequency in octave_frequencies]

    # Generate grid of noise values
    for grid_row in range(graphics.GRID_SIZE[1]):
        row_values = []
        for grid_col in range(graphics.GRID_SIZE[0]): 
            
            # Combine noise from all octaves (layers) into a single value
            combined_noise = 0
            for layer_index in range(len(noise_layers)):

                amplitude = 1 * PERSISTANCE**(layer_index)
                frequency_contribution = noise_layers[layer_index](
                    [grid_row / graphics.GRID_SIZE[1], grid_col / graphics.GRID_SIZE[0]]
                )
                
                combined_noise += amplitude * frequency_contribution
            
            combined_noise *= 255
            combined_noise = int(combined_noise)

            # Altitude min, max = 0, 255
            if combined_noise <= 0:
                combined_noise = 0
            elif combined_noise > 255:
                combined_noise = 255

            avg_alt += combined_noise
            row_values.append(combined_noise)

        heightmap.append(row_values)
    print(f"{round(avg_alt/(graphics.GRID_SIZE[0]*graphics.GRID_SIZE[1]))} alt avg")
    return heightmap