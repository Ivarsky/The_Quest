import os

import pygame as pg

from . import *
from .objects import BigAsteroid, Explosion, Scoreboard, SmallAsteroid, SpaceShip

from random import randint


class Scene:
    def __init__(self, screen: pg.Surface):
        self.display = screen

    def main_loop(self):
        pass


class Front(Scene):

    def __init__(self, screen: pg.Surface):
        super().__init__(screen)
        image_background = pg.image.load(os.path.join(
            "resources", "background", "bg-preview-big.png"))
        self.background = pg.transform.scale2x(image_background)
        self.font_file = os.path.join(
            "resources", "fonts", "PublicPixel-z84yD.ttf")
        self.clock = pg.time.Clock()

    def main_loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    #    if event.key == pg.K_ESCAPE:
                    #        print("Exiting")
                    #        return
                    if event.key == pg.K_SPACE:
                        return
                if event.type == pg.QUIT:
                    print("Exiting!")
                    pg.quit()

            self.draw_background()
            self.draw_title()
            self.draw_text1()
            self.draw_text2()
            pg.display.flip()
            self.clock.tick(FPS)

    def draw_background(self):
        self.display.blit(self.background, (0, 0))

    def draw_title(self):
        typography = pg.font.Font(self.font_file, 100)
        message = "The Quest"
        text = pg.font.Font.render(typography, message, True, C_YELLOW)
        text_width = text.get_width()
        pos_x = (WIDTH-text_width)/2
        pos_y = 0.15 * HEIGHT
        self.display.blit(text, (pos_x, pos_y))

    def draw_text1(self):
        typography = pg.font.Font(self.font_file, 16)
        message = "¡Usa flecha arriba y abajo para esquivar los obstáculos!"
        text = pg.font.Font.render(typography, message, True, C_YELLOW)
        text_width = text.get_width()
        pos_x = (WIDTH-text_width)/2
        pos_y = 0.50 * HEIGHT
        self.display.blit(text, (pos_x, pos_y))

    def draw_text2(self):
        typography = pg.font.Font(self.font_file, 16)
        message = "Pulsa Espacio para empezar a jugar"
        text = pg.font.Font.render(typography, message, True, C_YELLOW)
        text_width = text.get_width()
        pos_x = (WIDTH-text_width)/2
        pos_y = 0.75 * HEIGHT
        self.display.blit(text, (pos_x, pos_y))


class Story(Scene):

    def __init__(self, screen: pg.Surface):
        super().__init__(screen)
        image_background = pg.image.load(os.path.join(
            "resources", "background", "bg-preview-big.png"))
        self.background = pg.transform.scale2x(image_background)
        self.font_file = os.path.join(
            "resources", "fonts", "PublicPixel-z84yD.ttf")
        self.clock = pg.time.Clock()

    def main_loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    #    if event.key == pg.K_ESCAPE:
                    #        print("Exiting")
                    #        return
                    if event.key == pg.K_SPACE:
                        return
                if event.type == pg.QUIT:
                    print("Exiting!")
                    pg.quit()

            self.draw_background()
            self.draw_title()
            self.draw_text1()
            self.draw_text2()
            pg.display.flip()
            self.clock.tick(FPS)

    def draw_background(self):
        self.display.blit(self.background, (0, 0))

    def draw_title(self):
        typography = pg.font.Font(self.font_file, 18)
        message = "La Tierra es inhabitable y debemos abandonarla, para ello hemos construido una nave"
        text = pg.font.Font.render(typography, message, True, C_YELLOW)
        text_width = text.get_width()
        pos_x = (WIDTH-text_width)/2
        pos_y = 0.40 * HEIGHT
        self.display.blit(text, (pos_x, pos_y))

    def draw_text1(self):
        typography = pg.font.Font(self.font_file, 18)
        message = "y con ella viajaremos hacia otro mundo donde podremos prosperar"
        text = pg.font.Font.render(typography, message, True, C_YELLOW)
        text_width = text.get_width()
        pos_x = (WIDTH-text_width)/2
        pos_y = 0.50 * HEIGHT
        self.display.blit(text, (pos_x, pos_y))

    def draw_text2(self):
        typography = pg.font.Font(self.font_file, 16)
        message = "Pulsa Espacio para empezar"
        text = pg.font.Font.render(typography, message, True, C_YELLOW)
        text_width = text.get_width()
        pos_x = (WIDTH-text_width)/2
        pos_y = 0.75 * HEIGHT
        self.display.blit(text, (pos_x, pos_y))


class Game(Scene):

    def __init__(self, display):
        self.display = pg.display.set_mode(
            (WIDTH, HEIGHT))
        self.space_ship = SpaceShip()

        self.clock = pg.time.Clock()
        self.big_asteroid = BigAsteroid()
        self.small_asteroid = SmallAsteroid()
        self.score = Scoreboard()
        image_background = pg.image.load(os.path.join(
            "resources", "background", "bg-preview-big.png"))
        self.background = pg.transform.scale2x(image_background)
        self.explosion_group = pg.sprite.Group()

    def draw_background(self):
        self.display.blit(self.background, (0, 0))

    def make_explosion(self):
        explosion = Explosion(self.space_ship.rect.x, self.space_ship.rect.y)
        self.explosion_group.add(explosion)

    def collide(self):
        """
        Comprueba si el asteroide colisiona con la nave, resetea la posición del asteroide y resta un punto de vida
        """
        # colision entre asteroide grande y nave
        if pg.Rect.colliderect(self.big_asteroid.rect, self.space_ship.rect):
            self.space_ship.hit_hull()
            self.space_ship.hull_damage.ckeck_gameover_condition()
            self.make_explosion()

            if not self.space_ship.hull_damage.destroyed:
                self.make_explosion()
                self.big_asteroid.rect.x = WIDTH
                self.big_asteroid.rect.y = self.big_asteroid.rect.y = randint(
                    0, HEIGHT)
        # colision entre asteroide pequeño y nave
        if pg.Rect.colliderect(self.small_asteroid.rect, self.space_ship.rect):
            self.make_explosion()
            self.space_ship.hit_hull()
            self.space_ship.hull_damage.ckeck_gameover_condition()

            if not self.space_ship.hull_damage.destroyed:
                self.make_explosion()
                self.small_asteroid.rect.x = WIDTH
                self.small_asteroid.rect.y = self.small_asteroid.rect.y = randint(
                    0, HEIGHT)

    def main_loop(self):
        print("Starting game!")

        while True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    #    if event.key == pg.K_ESCAPE:
                    #        print("Exiting")
                    #        return
                    if event.key == pg.K_r:
                        self.score.initialize()
                        self.space_ship.hull_damage.initialize()

                if event.type == pg.QUIT:
                    print("Exiting")
                    pg.quit()

            # mueve asteroides y comprueba si chocan con la nave
            if self.space_ship.hull_damage.destroyed == False:
                self.big_asteroid.update()
                self.small_asteroid.update()
                if self.score.win == False:
                    self.collide()
            # para el asteroide
            else:
                self.big_asteroid.rect.x = WIDTH
                self.big_asteroid.rect.y = randint(0, HEIGHT)
                self.small_asteroid.rect.x = WIDTH
                self.big_asteroid.rect.y = randint(0, HEIGHT)

            # Resetea asteroides y marca si esquivados
            if self.score.win == False:
                if self.big_asteroid.rect.x <= 1:
                    self.score.add_score()
                    self.score.check_win_condition()
                    if self.big_asteroid.rect.x <= 0:
                        self.big_asteroid.rect.x = WIDTH
                        self.big_asteroid.rect.y = randint(0, HEIGHT)

            if self.score.win == False:
                if self.small_asteroid.rect.x <= 1:
                    self.score.add_score()
                    self.score.check_win_condition()
                    if self.small_asteroid.rect.x <= 0:
                        self.small_asteroid.speed = randint(7, 10)
                        self.small_asteroid.rect.x = WIDTH
                        self.small_asteroid.rect.y = randint(0, HEIGHT)

            # dibuja el fondo
            self.draw_background()
            # dibuja la nave
            if not self.space_ship.hull_damage.destroyed:
                self.space_ship.update()
                self.display.blit(self.space_ship.image, self.space_ship.rect)
            # dibuja los asteroides
            self.display.blit(self.big_asteroid.image, self.big_asteroid.rect)
            self.display.blit(self.small_asteroid.image,
                              self.small_asteroid.rect)

            # dibuja explosion
            self.explosion_group.draw(self.display)
            self.explosion_group.update()
            # if self.explosion_flag == True:
            #    self.make_explosion()
            #    self.explosion_group.update()

            # dibuja los puntos para ganar (asteroides esquivados)
            self.score.draw(self.display)
            # dibuja los puntos para perder (golpes a la nave)
            self.space_ship.hull_damage.draw(self.display)

            pg.display.flip()
            self.clock.tick(FPS)


class HallOfFame(Scene):
    def main_loop(self):
        while True:
            for event in pg.event.get():
                # if event.type == pg.KEYDOWN:
                #    if event.key == pg.K_ESCAPE:
                #        print("Exiting")
                #        return
                if event.type == pg.QUIT:
                    print("Exiting")
                    pg.quit()
            self.display.fill(C_GREEN)
            pg.display.flip()
