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
            self.typography, "HP "+str(self.points), True, C_WHITE)
        pos_x = (WIDTH - text.get_width())/8
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
        self.rect.x = self.rect.x - ASTEROID_SPEED


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
        self.rect.x = self.rect.x - self.speed


class AlienShip(Sprite):

    fps_animation = 12
    limit_iteration = FPS / fps_animation
    iteration = 0

    def __init__(self):
        super().__init__()
        self.score = Scoreboard()
        self.space_ship = SpaceShip()
        self.sprites = []
        for i in range(5):
            self.sprites.append(pg.transform.scale2x(pg.image.load(
                os.path.join("resources", "enemy", "sprites", f"enemy{i}.png"))))

        self.next_image = 0
        self.image = self.sprites[self.next_image]
        self.x = WIDTH
        self.y = randint(0, HEIGHT)
        self.rect = self.image.get_rect(x=self.x, y=self.y)
        self.speed = ASTEROID_SPEED * 1.5

    def update(self):
        self.rect.x = self.rect.x - self.speed
        self.iteration += 1
        if self.iteration == self.limit_iteration:
            self.next_image += 1
            if self.next_image >= len(self.sprites) - 1:
                self.next_image = 0
            self.image = self.sprites[self.next_image]
            self.iteration = 0


class Scoreboard:
    """
    guarda la puntuacion y la pinta
    """

    def __init__(self):
        self.initialize()
        pg.font.init()
        font_file = os.path.join("resources", "fonts", "PublicPixel-z84yD.ttf")
        self.typography = pg.font.Font(font_file, 50)
        self.typography_endgame = pg.font.Font(font_file, 18)

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
            self.typography, "Puntos "+str(self.points), True, C_YELLOW)
        pos_x = ((WIDTH - text.get_width())/4) + WIDTH/2
        pos_y = LATERAL_MARGIN
        pg.surface.Surface.blit(screen, text, (pos_x, pos_y))

        if self.win == True:
            text = pg.font.Font.render(
                self.typography_endgame, "Bien hecho! abandonamos el sistema solar!", True, C_YELLOW)
            text1 = pg.font.Font.render(
                self.typography_endgame, "Ahora emprenderemos nuestro largo viaje, Nova Terra nos espera!", True, C_YELLOW)
            text2 = pg.font.Font.render(
                self.typography_endgame, "Espacio para continuar", True, C_YELLOW)
            pos_x = (WIDTH - text.get_width())/2
            pos_y = (HEIGHT - text.get_height())/2

            pos_x1 = (WIDTH - text1.get_width())/2
            pos_y1 = pos_y + 25

            pos_x2 = (WIDTH - text2.get_width())/2
            pos_y2 = pos_y1 + 50

            pg.surface.Surface.blit(screen, text, (pos_x, pos_y))
            pg.surface.Surface.blit(screen, text1, (pos_x1, pos_y1))
            pg.surface.Surface.blit(screen, text2, (pos_x2, pos_y2))


class Explosion(Sprite):

    fps_animation = 12
    limit_iteration = FPS / fps_animation
    iteration = 0

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.space_ship = SpaceShip()
        self.sprites = []
        for i in range(6):
            self.sprites.append(pg.transform.scale2x(pg.image.load(
                os.path.join("resources", "explosion", "sprites", f"explosion{i}.png"))))

        self.next_image = 0
        self.image = self.sprites[self.next_image]
        self.rect = self.image.get_rect(x=pos_x, y=pos_y)

    def update(self):
        self.iteration += 1
        if self.iteration == self.limit_iteration:
            self.next_image += 1
            if self.next_image >= len(self.sprites) - 1:
                self.kill()
            self.image = self.sprites[self.next_image]
            self.iteration = 0
