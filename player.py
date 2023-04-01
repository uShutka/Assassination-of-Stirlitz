import time
from settings import *
import pygame
import math
from map import world_map

reset_num = lambda num, num_res: int(round(num, num_res)) if round(num, num_res) <= num else int(round(num, num_res) - 100)
run_music = False
is_kill = False
time_play = time.time()


def play_sound_steps():
    pygame.mixer.Sound('sounds/step.mp3').play()
    return time.time()


# Check if the player is trying to go into the wall
def check(player_position):
    for x, y in world_map:
        if (reset_num(player_position[0], -2), reset_num(player_position[1], -2)) == (x, y):
            return False

    return True


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        """Getting a player's position"""
        return self.x, self.y

    def movement(self):
        """Register key presses and perform any movements"""
        global time_play
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()

        if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d] and time_play - time.time() > 1.8:
            pygame.mixer.stop()

        if keys[pygame.K_w]:
            player_x = self.x + player_speed * cos_a
            player_y = self.y + player_speed * sin_a
            if check((player_x, player_y)):

                if time.time() - time_play > 1.8:
                    time_play = play_sound_steps()

                self.x = player_x
                self.y = player_y

        if keys[pygame.K_s]:
            player_x = self.x - player_speed * cos_a
            player_y = self.y - player_speed * sin_a
            if check((player_x, player_y)):
                if time.time() - time_play > 2:
                    time_play = play_sound_steps()

                self.x = player_x
                self.y = player_y

        if keys[pygame.K_a]:
            player_x = self.x + player_speed * sin_a
            player_y = self.y - player_speed * cos_a
            if check((player_x, player_y)):
                if time.time() - time_play > 2:
                    time_play = play_sound_steps()

                self.x = player_x
                self.y = player_y

        if keys[pygame.K_d]:
            player_x = self.x - player_speed * sin_a
            player_y = self.y + player_speed * cos_a
            if check((player_x, player_y)):
                if time.time() - time_play > 2:
                    time_play = play_sound_steps()

                self.x = player_x
                self.y = player_y

        if keys[pygame.K_e]:
            return True

        if keys[pygame.K_LEFT]:
            self.angle -= 0.02

        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

        self.angle %= pi_multiply_2

    def shoot(self, enemy):
        """Shooting"""
        for i in range(WIDTH):
            x_p, y_p = (int(self.pos[0] + i * math.cos(self.angle)), int(self.pos[1] + i * math.sin(self.angle)))
            rod_coord = round(x_p, -1), round(y_p, -1)
            if rod_coord == enemy:
                global is_kill
                is_kill = True
                return True

        return False