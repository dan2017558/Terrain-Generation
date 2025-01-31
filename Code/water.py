import graphics

cleared = graphics.GRID_SIZE[0]*graphics.GRID_SIZE[1]

# Retrieve surrounding cells
def clear_water(heightmap, water_level):
    global cleared
    new_water = []
    for grid_row in range(graphics.GRID_SIZE[1]):
        for grid_col in range(graphics.GRID_SIZE[0]): 
            if heightmap[grid_row][grid_col] <= water_level and heightmap[grid_row][grid_col] != 0:  # Do not process water cells
                try:
                    # North, south, east, and west cells
                    if heightmap[grid_row][grid_col-1] <= water_level and heightmap[grid_row+1][grid_col] <= water_level and heightmap[grid_row][grid_col+1] <= water_level and heightmap[grid_row-1][grid_col] <= water_level:
                        new_water.append([grid_row, grid_col])
                except IndexError:  # edges

                    pass


    for i in new_water:
        heightmap[i[0]][i[1]] = 0
    cleared = len(new_water)
    print(f"{cleared} island cells cleared out of {graphics.GRID_SIZE[0]*graphics.GRID_SIZE[1]} cells")