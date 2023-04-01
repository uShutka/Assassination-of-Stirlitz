import pygame
from settings import *
from map import mini_map

class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.Font('fonts/RubikMonoOne-Regular.ttf', 21)
        self.textures = {'W': pygame.image.load('images/wall.png').convert(),
                         '#': pygame.image.load('images/door.png').convert()
                         }
        self.gun = pygame.image.load('images/barrel.png').convert_alpha()

    def background(self):
        """Отрисовываем фон"""
        pygame.draw.rect(self.sc, SKY_BLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.sc, DARK_GRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, world_object):
        """Отрисовываем мир в 3д с помощью рейкастинга"""
        try:
            for obj in sorted(world_object, key=lambda n: n[0], reverse=True):
                if obj[0]:
                    _, object_world, object_pos = obj
                    self.sc.blit(object_world, object_pos)
        except:
            pass


    def fps(self, clock):
        """Draw the fps count in the corner of the screen"""
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.sc.blit(render, (WIDTH - len(display_fps) * 21, 5))

    def kill(self):
        """Drawing the murder in the screen"""
        text = "Congratulations! You made the kill. Now head for the door."
        render_win_text = self.font.render(text, 0, RED)
        render_ok_text = self.font.render('OK', 0, BLACK)
        pygame.draw.rect(self.sc, WHITE, (len(text), HALF_HEIGHT- 21,  21 * (len(text)-8), 100))
        pygame.draw.rect(self.sc, RED, (WIDTH - len(text) * 2 - 100, HALF_HEIGHT + len(text) - 30, 90, 45))
        self.sc.blit(render_win_text, (len(text), HALF_HEIGHT- 21))
        self.sc.blit(render_ok_text, (WIDTH - len(text) * 2 - 75, HALF_HEIGHT + len(text) - 20))

    def bullet(self):
        """bullet"""
        g_surf = pygame.transform.scale(self.gun, (self.gun.get_width() * 10, self.gun.get_height() * 10))
        gun_rect = g_surf.get_rect(center=(HALF_WIDTH, HEIGHT-320))
        self.sc.blit(g_surf, gun_rect)

    def mini_map(self, player):
        """Drawing a mini-map"""
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // scale_of_minimap, player.y // scale_of_minimap
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                 map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, RED, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, GREEN, (x, y, tile_of_map, tile_of_map))
        self.sc.blit(self.sc_map, position_of_map)

    def press_e(self):
        """Click on e"""
        text = "Press e to pass"
        render = self.font.render(text, 0, RED)
        pygame.draw.rect(self.sc, WHITE, (HALF_WIDTH - len(text) * 8, HALF_HEIGHT,  21 * (len(text)) + 10, 27))
        self.sc.blit(render, (HALF_WIDTH - len(text) * 8, HALF_HEIGHT))

    def not_press_e(self):
        """You can't go any further"""
        text = "You have not yet defeated all your opponents."
        render = self.font.render(text, 0, RED)
        pygame.draw.rect(self.sc, WHITE, (HALF_WIDTH - len(text) * 9, HALF_HEIGHT,  21 * (len(text)-8) + 68, 27))
        self.sc.blit(render, (HALF_WIDTH - len(text) * 9, HALF_HEIGHT))

    def win(self):
        """Victory"""
        text = "You are win!"
        render = self.font.render(text, 0, RED)
        pygame.draw.rect(self.sc, WHITE, (HALF_WIDTH - len(text) * 8, HALF_HEIGHT,  21 * (len(text)-8) + 143, 27))
        self.sc.blit(render, (HALF_WIDTH - len(text) * 8, HALF_HEIGHT))
