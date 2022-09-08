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


"""
class SpaceshipSprite(Sprite):
    def __init__(self, ):
        super().__init__()
        image_path = os.path.join(
            "resources", "player", "sprites", "player1.png")
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect(centerx=(WIDTH-(WIDTH-LATERAL_MARGIN)))

    def update(self):
        pass
"""


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
        self.centerx = LATERAL_MARGIN*2
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


class Asteroid(pg.Rect):
    def __init__(self):
        super(Asteroid, self).__init__(WIDTH-ASTEROID_SIZE, randint(HEIGHT -
                                                                    (HEIGHT-ASTEROID_SIZE), HEIGHT-ASTEROID_SIZE), ASTEROID_SIZE, ASTEROID_SIZE)

    def move(self):
        self.x = self.x - ASTEROID_SPEED

    # Resetea la posicion del asteroide al borde de la pantalla a altura aleatoria
    def reset(self):
        self.x = WIDTH
        self.y = randint(HEIGHT - (HEIGHT-ASTEROID_SIZE), HEIGHT-ASTEROID_SIZE)


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

    def add_score(self):
        """
        Marca punto
        """
        self.points += 1
        print(f"{self.points} Asteroids dodged!")

    def initialize(self):
        self.points = 0
        self.win = False

    def draw(self, screen):
        text = pg.font.Font.render(
            self.typography, str(self.points), True, C_WHITE)
        pos_x = ((WIDTH - text.get_width())/4) + WIDTH/2
        pos_y = LATERAL_MARGIN
        pg.surface.Surface.blit(screen, text, (pos_x, pos_y))

        if self.win == True:
            text = pg.font.Font.render(
                self.typography_endgame, "You Win!", True, C_WHITE)
            pos_x = (WIDTH - text.get_width())/2
            pos_y = (HEIGHT - text.get_height())/2
            pg.surface.Surface.blit(screen, text, (pos_x, pos_y))
