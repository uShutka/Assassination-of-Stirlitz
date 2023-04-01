import pygame
from settings import *


class Sprites:
    def __init__(self):
        self.sprite_types = {
            'nazi': [pygame.image.load(f'images/{i}.png').convert_alpha() for i in range(8)],
            'dead_nazi': [pygame.image.load(f'images/dead_nazi.png').convert_alpha() for i in range(8)]
        }
        sprite_nazi = SpriteObject(self.sprite_types['nazi'], False, (7, 4), -0.2, 0.7)
        self.list_of_objects = [
            sprite_nazi,
        ]
        from player import is_kill
        if is_kill:
            self.list_of_objects.append(SpriteObject(self.sprite_types['dead_nazi'], False, (7, 4), -0.2, 0.7))
            self.list_of_objects.remove(sprite_nazi)



class SpriteObject:
    def __init__(self, objection, static, pos, shift, scale_sprite):
        self.object = objection
        self.static = static
        self.pos = self.x, self.y = pos[0] * size_of_box, pos[1] * size_of_box
        self.shift = shift
        self.scale = scale_sprite

        if not static:
            self.sprite_angles = [frozenset(range(i, i + 45)) for i in range(0, 360, 45)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}

    def object_locate(self, player, walls):
        dx, dy = self.x - player.x, self.y - player.y
        distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)
        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += pi_multiply_2

        delta_rays = int(gamma / delta_of_angle)
        current_ray = ray_of_center + delta_rays
        distance_to_sprite *= math.cos(HALF_FOV - current_ray * delta_of_angle)

        if 0 <= current_ray <= num_rays - 1 and distance_to_sprite < walls[current_ray][0]:
            proj_height = min(int(coefficient / distance_to_sprite * self.scale), 2 * HEIGHT)
            half_proj_height = proj_height // 2
            shift = half_proj_height * self.shift

            if not self.static:
                if theta < 0:
                    theta += pi_multiply_2
                theta = 360 - int(math.degrees(theta))

                for angles in self.sprite_angles:
                    if theta in angles:
                        self.object = self.sprite_positions[angles]
                        break
            sprite_pos = (current_ray * scale - half_proj_height, HALF_HEIGHT - half_proj_height + shift)
            if type(self.object) != list:
                sprite = pygame.transform.scale(self.object, (proj_height, proj_height))
            else:
                return None

            return distance_to_sprite, sprite, sprite_pos
        else:
            return False,

    @property
    def get_position_sprite(self):
        return self.pos