import os

import pygame as pg

from . import *
from .objects import Asteroid, Scoreboard, SpaceShip


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


class Game(Scene):

    def __init__(self, display):
        self.display = pg.display.set_mode(
            (WIDTH, HEIGHT))
        self.space_ship = SpaceShip()
        self.clock = pg.time.Clock()
        self.asteroid = Asteroid()
        self.score = Scoreboard()
        image_background = pg.image.load(os.path.join(
            "resources", "background", "bg-preview-big.png"))
        self.background = pg.transform.scale2x(image_background)

    def draw_background(self):
        self.display.blit(self.background, (0, 0))

    def collide(self):
        """
        Comprueba si el asteroide colisiona con la nave, resetea la posición del asteroide y resta un punto de vida
        """
        if pg.Rect.colliderect(self.asteroid, self.space_ship):
            self.space_ship.hit_hull()
            self.space_ship.hull_damage.ckeck_gameover_condition()
            if not self.space_ship.hull_damage.destroyed:
                self.asteroid.reset()

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

            if self.score.win == False and self.space_ship.hull_damage.destroyed == False:
                self.asteroid.move()
                self.collide()
            if self.asteroid.x <= 0:
                self.score.add_score()
                self.score.check_win_condition()
                self.asteroid.reset()

            # self.display.fill(C_BLACK)   <---- DELETE
            # dibuja el fondo
            self.draw_background()
            # dibuja la nave
            if not self.space_ship.hull_damage.destroyed:
                self.space_ship.update()
                self.display.blit(self.space_ship.image, self.space_ship.rect)
            # dibuja los asteroides
            pg.draw.rect(self.display, C_WHITE, self.asteroid)
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
