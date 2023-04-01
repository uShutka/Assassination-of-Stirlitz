import pygame
from settings import *
from map import world_map


def mapping(a, b):
    """Checking the contact"""
    return (a // size_of_box) * size_of_box, (b // size_of_box) * size_of_box


def ray_casting(player_position, angle_of_player, textures):
    """The main function of drawing rectangles according to the 2D map described in the map file"""
    walls = []
    ox, oy = player_position
    xm, ym = mapping(ox, oy)
    cur_angle = angle_of_player - HALF_FOV
    for ray in range(num_rays):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        # check the intersection with the verticals using the Brenzenham algorithm
        x, dx = (xm + size_of_box, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, size_of_box):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break

            x += dx * size_of_box

        # check the intersection with the horizontals by the Brenzenham algorithm
        y, dy = (ym + size_of_box, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, HEIGHT, size_of_box):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break

            y += dy * size_of_box

        # projection
        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % size_of_box
        depth *= math.cos(angle_of_player - cur_angle)
        depth = max(depth, 0.000001)
        proj_height = min(int(coefficient / depth), 2 * HEIGHT)
        wall_column = textures[texture].subsurface(offset * texture_sl, 0, texture_sl, texture_hg)
        wall_column = pygame.transform.scale(wall_column, (scale, proj_height))
        wall_pos = (ray * scale, HALF_HEIGHT - proj_height // 2)
        walls.append((depth, wall_column, wall_pos))
        cur_angle += delta_of_angle

    return walls
