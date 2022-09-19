import csv
import os

import pygame as pg
from pygame.sprite import Sprite

from . import *
from .records import DBManager

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
            # TODO: que la nave desaparezca al explotar
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
            self.typography, "HP "+str(3 - self.points), True, C_WHITE)
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

    fps_animation = 12
    limit_iteration = FPS / fps_animation
    iteration = 0

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
        self.planet = Planet()
        self.angle = 1

    def update(self):
        key_status = pg.key.get_pressed()
        if self.planet.planet_in_position != True:
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

    def rot_center(self):
        if self.angle < 180:
            self.angle += 3 % 180
        self.rect = self.image.get_rect(center=self.rect.center)
        self.image = pg.transform.rotate(self.image, self.angle)


class BigAsteroid(Sprite):
    def __init__(self):
        super().__init__()
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
        image_path = os.path.join(
            "resources", "asteroids", "asteroid-small.png")
        self.image = pg.transform.scale2x(pg.image.load(image_path))
        self.x = WIDTH
        self.y = randint(0, HEIGHT)
        self.rect = self.image.get_rect(x=self.x, y=self.y)
        self.speed = ASTEROID_SPEED * 1.5

    def update(self):
        self.rect.x = self.rect.x - self.speed


class BigAlienShip(Sprite):

    fps_animation = 12
    limit_iteration = FPS / fps_animation
    iteration = 0

    def __init__(self):
        super().__init__()
        self.sprites = []
        for i in range(5):
            self.sprites.append(pg.transform.scale2x(pg.image.load(
                os.path.join("resources", "enemy", "sprites", f"enemy{i}.png"))))

        self.next_image = 0
        self.image = self.sprites[self.next_image]
        self.x = WIDTH
        self.y = randint(0, HEIGHT)
        self.rect = self.image.get_rect(x=self.x, y=self.y)
        self.speed_ship = ASTEROID_SPEED * 3

    def update(self):
        self.rect.x = self.rect.x - self.speed_ship
        self.iteration += 1
        if self.iteration == self.limit_iteration:
            self.next_image += 1
            if self.next_image >= len(self.sprites) - 1:
                self.next_image = 0
            self.image = self.sprites[self.next_image]
            self.iteration = 0


class SmallAlienShip(Sprite):

    fps_animation = 12
    limit_iteration = FPS / fps_animation
    iteration = 0

    def __init__(self):
        super().__init__()
        self.sprites = []
        for i in range(5):
            self.sprites.append(pg.image.load(
                os.path.join("resources", "enemy", "sprites", f"enemy{i}.png")))

        self.next_image = 0
        self.image = self.sprites[self.next_image]
        self.x = WIDTH
        self.y = randint(0, HEIGHT)
        self.rect = self.image.get_rect(x=self.x, y=self.y)
        self.speed_small_ship = ASTEROID_SPEED * 4

    def update(self):
        self.rect.x = self.rect.x - self.speed_small_ship
        self.iteration += 1
        if self.iteration == self.limit_iteration:
            self.next_image += 1
            if self.next_image >= len(self.sprites) - 1:
                self.next_image = 0
            self.image = self.sprites[self.next_image]
            self.iteration = 0


class Scoreboard1:
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


class Scoreboard2:
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
            # FIXME: que los textos aparezcan en el momento adecuado (mejor creo una clase aparte)
            text1 = pg.font.Font.render(
                self.typography_endgame, "¡Lo has conseguido! Aterrizando...", True, C_YELLOW)

            text2 = pg.font.Font.render(
                self.typography_endgame, "¡Un nuevo planeta!, la humanidad vuelve a tener esperanza", True, C_YELLOW)

            text3 = pg.font.Font.render(
                self.typography_endgame, "Espacio para continuar", True, C_YELLOW)

            pos_x1 = (WIDTH - text1.get_width())/2
            pos_y1 = HEIGHT * 0.25
            pos_x2 = (WIDTH - text2.get_width())/2
            pos_y2 = HEIGHT * 0.35
            pos_x3 = (WIDTH - text3.get_width())/2
            pos_y3 = HEIGHT * 0.75

            pg.surface.Surface.blit(screen, text1, (pos_x1, pos_y1))
            pg.surface.Surface.blit(screen, text2, (pos_x2, pos_y2))
            pg.surface.Surface.blit(screen, text3, (pos_x3, pos_y3))


class Explosion(Sprite):

    fps_animation = 12
    limit_iteration = FPS / fps_animation
    iteration = 0

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.space_ship = SpaceShip()
        self.explosion_sound = pg.mixer.Sound(os.path.join(
            "resources", "Sound FX", "shot 1.wav"))
        self.sprites = []
        for i in range(6):
            self.sprites.append(pg.transform.scale2x(pg.image.load(
                os.path.join("resources", "explosion", "sprites", f"explosion{i}.png"))))

        self.next_image = 0
        self.image = self.sprites[self.next_image]
        self.rect = self.image.get_rect(x=pos_x, y=pos_y)

    def update(self):
        self.explosion_sound.play()
        #self.iteration += 1
        # if self.iteration == self.limit_iteration:
        self.next_image += 1
        if self.next_image >= len(self.sprites) - 1:
            self.kill()
        self.image = self.sprites[self.next_image]
        #self.iteration = 0


class Planet(Sprite):
    def __init__(self):
        super().__init__()
        image_path = os.path.join("resources", "planet", "planet.png")
        self.image = pg.transform.scale(
            pg.image.load(image_path), (PLANET_HEIGHT, PLANET_WIDTH))
        self.x = WIDTH
        self.y = 0
        self.rect = self.image.get_rect(x=self.x, y=self.y)
        self.planet_in_position = False

    def update(self):
        if self.rect.x >= WIDTH/2:
            self.rect.x = self.rect.x - 5
        if self.rect.x <= WIDTH/2:
            self.planet_in_position = True
            self.rect.x = WIDTH/2


class InputBox():
    def __init__(self, screen: pg.Surface, text_color="white", background_color="black", title=""):
        pg.font.init()
        font_file = os.path.join("resources", "fonts", "PublicPixel-z84yD.ttf")
        self.typography = pg.font.Font(font_file, 20)
        self.text = ""
        self.title = title
        self.background_color = background_color
        self.text_color = text_color
        self.display = screen
        self.padding = 30
        self.create_fixed_items()

    def create_fixed_items(self):
        # titulo
        self.titulo = self.typography.render(
            "Nuevo record!, introduce tu nombre: ", True, self.text_color, self.background_color)
        self.x_title = (WIDTH-self.title.get_width())//2
        self.y_title = (HEIGHT-self.title.get_height()//2)

        # rectangulo de fondo:
        x_background = self.x_title - self.padding
        y_background = self.y_title = self.padding
        w_background = self.title.get_width() + self.padding*2
        h_background = self.title.get_height() * 2 + self.padding*2
        self.background = pg.Rect(
            x_background, y_background, w_background, h_background)

    def draw(self):
        # pequeño recuadro aparte para ir repintandolo
        pg.draw.rect(self.display, self.background_color, self.background)
        self.display.blit(self.title, (self.x_title, self.y_title))

        text_surface = self.typography.render(
            self.text, True, self.text_color, self.background_color)
        pos_x = self.x_title
        pos_y = self.y_title + self.title.get_height()
        self.display.blit(text_surface, (pos_x, pos_y))

    def get_text(self):
        leave = False
        while not leave:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE and len(self.text) > 0:
                        self.text = self.text[:-1]
                    elif event.key == pg.K_RETURN:
                        leave = True
                    else:
                        self.text += event.unicode
            self.draw()
            pg.display.flip()
        return self.text
