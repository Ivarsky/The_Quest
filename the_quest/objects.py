import os

import pygame as pg
from pygame.sprite import Sprite

from . import *

from random import randint


class HullPoints:
    """
    Guarda los puntos de vida de la nave y los pinta
    """

    def __init__(self):
        self.initialize()
        pg.font.init()
        font_file = os.path.join("resources", "fonts", "PublicPixel-z84yD.ttf")
        self.typography = pg.font.Font(font_file, 50)
        self.typography_endgame = pg.font.Font(font_file, 100)

    def ckeck_gameover_condition(self):
        if self.points == MAX_HULL_HITPOINTS:
            print("Ship Destroyed!, GAME OVER")
            self.destroyed = True
        else:
            print(
                f"Collision! {MAX_HULL_HITPOINTS - self.points} hull points left!")

    def initialize(self):
        self.points = 0
        self.destroyed = False

    def draw(self, screen):
        text = pg.font.Font.render(
            self.typography, str(self.points), True, C_WHITE)
        pos_x = (WIDTH - text.get_width())/4
        pos_y = LATERAL_MARGIN
        pg.surface.Surface.blit(screen, text, (pos_x, pos_y))

        if self.destroyed == True:
            text = pg.font.Font.render(
                self.typography_endgame, "Game Over", True, C_WHITE)
            pos_x = (WIDTH - text.get_width())/2
            pos_y = (HEIGHT - text.get_height())/2
            pg.surface.Surface.blit(screen, text, (pos_x, pos_y))


class SpaceShip(Sprite):

    def __init__(self):
        super(). __init__()
        self.image_path_straight = os.path.join(
            "resources", "player", "sprites", "player1.png")
        self.image_path_down = os.path.join(
            "resources", "player", "sprites", "player2.png")
        self.image_path_up = os.path.join(
            "resources", "player", "sprites", "player3.png")

        self.image = pg.transform.scale2x(
            pg.image.load(self.image_path_straight))
        self.centerx = LATERAL_MARGIN*3
        self.centery = HEIGHT/2
        self.rect = self.image.get_rect(
            centerx=self.centerx, centery=self.centery)
        self.speed = 5
        self.hull_damage = HullPoints()

    def update(self):
        key_status = pg.key.get_pressed()
        if key_status[pg.K_UP]:
            self.rect.y -= self.speed
            self.image = pg.transform.scale2x(
                pg.image.load(self.image_path_up))
            if self.rect.top < 0:
                self.rect.top = 0

        elif key_status[pg.K_DOWN]:
            self.rect.y += self.speed
            self.image = pg.transform.scale2x(pg.image.load(
                self.image_path_down))
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT

        else:
            self.image = pg.transform.scale2x(pg.image.load(
                self.image_path_straight))

    def hit_hull(self):
        self.hull_damage.points += 1


class BigAsteroid(Sprite):
    def __init__(self):
        super().__init__()
        self.score = Scoreboard()
        image_path = os.path.join("resources", "asteroids", "asteroid.png")
        self.image = pg.transform.scale2x(pg.image.load(image_path))
        self.x = WIDTH
        self.y = randint(0, HEIGHT)
        self.rect = self.image.get_rect(x=self.x, y=self.y)

    def update(self):
        if not self.score.check_win_condition == True:
            self.rect.x = self.rect.x - ASTEROID_SPEED
            # if self.rect.x <= 0:
            #    self.rect.x = WIDTH
            #    self.rect.y = randint(0, HEIGHT)


class SmallAsteroid(Sprite):
    def __init__(self):
        super().__init__()
        self.score = Scoreboard()
        self.space_ship = SpaceShip()
        image_path = os.path.join(
            "resources", "asteroids", "asteroid-small.png")
        self.image = pg.transform.scale2x(pg.image.load(image_path))
        self.x = WIDTH
        self.y = randint(0, HEIGHT)
        self.rect = self.image.get_rect(x=self.x, y=self.y)
        self.speed = ASTEROID_SPEED * 1.5

    def update(self):
        if not self.score.check_win_condition == True:
            self.rect.x = self.rect.x - self.speed
            # if self.rect.x <= 0:
            #    self.speed = randint(7, 10)
            #    self.rect.x = WIDTH
            #    self.rect.y = randint(0, HEIGHT)


class Scoreboard:
    """
    guarda la puntuacion y la pinta
    """

    def __init__(self):
        self.initialize()
        pg.font.init()
        font_file = os.path.join("resources", "fonts", "PublicPixel-z84yD.ttf")
        self.typography = pg.font.Font(font_file, 50)
        self.typography_endgame = pg.font.Font(font_file, 50)

    def check_win_condition(self):
        if self.points == WIN_SCORE:
            self.win = True
            print("WIN!")

    def initialize(self):
        self.points = 0
        self.win = False

    def add_score(self):
        """
        Marca punto
        """
        self.points = self.points + 1
        print(f"{self.points} Asteroids dodged!")

    def draw(self, screen):
        text = pg.font.Font.render(
            self.typography, str(self.points), True, C_YELLOW)
        pos_x = ((WIDTH - text.get_width())/4) + WIDTH/2
        pos_y = LATERAL_MARGIN
        pg.surface.Surface.blit(screen, text, (pos_x, pos_y))

        if self.win == True:
            text = pg.font.Font.render(
                self.typography_endgame, "You Win!", True, C_WHITE)
            pos_x = (WIDTH - text.get_width())/2
            pos_y = (HEIGHT - text.get_height())/2
            pg.surface.Surface.blit(screen, text, (pos_x, pos_y))


class Explosion(Sprite):

    fps_animation = 12
    limit_iteration = FPS / fps_animation
    iteration = 0

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.space_ship = SpaceShip()
        self.sprites = []
        for i in range(5):
            self.sprites.append(pg.transform.scale2x(pg.image.load(
                os.path.join("resources", "explosion", "sprites", f"explosion{i}.png"))))

        self.next_image = 0
        self.image = self.sprites[self.next_image]
        self.rect = self.image.get_rect(x=pos_x, y=pos_y)

    def update(self):
        self.iteration += 1
        if self.iteration == self.limit_iteration:
            self.next_image += 1
            if self.next_image >= len(self.sprites):
                self.kill()
            self.image = self.sprites[self.next_image]
            self.iteration = 0
