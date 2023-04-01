import math

# Basic parameters
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
size_of_box = 100

# MiniMap Options
scale_of_minimap = 5
tile_of_map = size_of_box // scale_of_minimap
position_of_map = (0, HEIGHT - HEIGHT // scale_of_minimap)

# Ray-casting parameters
FOV = math.pi / 3
HALF_FOV = FOV / 2
num_rays = 300
maximal_depth = 800
delta_of_angle = FOV / num_rays
distance = num_rays / (2 * math.tan(HALF_FOV))
coefficient = 1.5 * distance * size_of_box
scale = WIDTH // num_rays

# Player Parameters
player_pos = (HALF_WIDTH, HALF_HEIGHT+50)
player_angle = 0
player_speed = 0.5

# Textures
texture_wd = 1184
texture_hg = 1184
texture_sl = texture_wd // size_of_box

# Sprite settings
pi_multiply_2 = math.pi * 2
ray_of_center = num_rays // 2 - 1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
SKY_BLUE = (0, 186, 255)
YELLOW = (220, 220, 0)

