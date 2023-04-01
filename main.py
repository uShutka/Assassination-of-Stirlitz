import time
import pygame
from settings import *
from player import Player
import math
from map import world_map
from drawing import Drawing
from sprites import *
from ray_casting import ray_casting
import sys

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // scale_of_minimap, HEIGHT // scale_of_minimap))
sprite = Sprites()
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)
pygame.mixer.music.set_volume(1)
time_2 = time.time()
is_win = False
is_window = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.fill(BLACK)
    drawing.background()
    response = player.movement()
    walls = ray_casting(player.pos, player.angle, drawing.textures)
    world = walls + [obj.object_locate(player, walls) for obj in sprite.list_of_objects]
    drawing.world(world)
    drawing.fps(clock)
    drawing.bullet()
    drawing.mini_map(player)

    if response and 200 > player.pos[0] and 200 > player.pos[1] and is_win:
        pygame.mixer.Sound('sounds/win.mp3').play()
        drawing.win()
        pygame.display.flip()
        time.sleep(5)
        sys.exit()

    if 200 > player.pos[0] and 200 > player.pos[1]:
        if is_win:
            drawing.press_e()
        else:
            drawing.not_press_e()

    if is_window:
        drawing.kill()
        if event.type == pygame.MOUSEBUTTONUP:
            if WIDTH - 168 - event.pos[0] <= 90 and HEIGHT - 328 - event.pos[1] <= 60:
                is_win = True
                is_window = False

    elif event.type == pygame.MOUSEBUTTONUP:
        time_1 = time.time()
        if time_1 - time_2 > 0.05:
            pygame.mixer.Sound('sounds/shoot.mp3').play()
            from player import is_kill
            if not is_kill:
                pos = [obj.get_position_sprite for obj in sprite.list_of_objects][0]

                if player.shoot(pos):
                    drawing.kill()
                    pygame.display.flip()
                    sprite = Sprites()
                    is_window = True


        time_2 = time.time()

    pygame.display.flip()
    clock.tick()