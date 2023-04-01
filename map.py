from settings import *

text_map = [
    'W#WWWWWWWWWW',
    'W..........W',
    'W..........W',
    'W..........W',
    'W..........W',
    'W..........W',
    'W..........W',
    'WWWWWWWWWWWW'
]


world_map = {}
mini_map = set()

# find the coordinates of the upper left point of the square of the part of the map labeled W
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map[(i * size_of_box, j * size_of_box)] = 'W'
            mini_map.add((i * tile_of_map, j * tile_of_map))

        elif char == '#':
            world_map[(i * size_of_box, j * size_of_box)] = '#'



