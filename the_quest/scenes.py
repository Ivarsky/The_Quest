import os
import pygame as pg

from the_quest import *
from the_quest.objects import Asteroid, Scoreboard, SpaceShip


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
        self.clock = pg.time.Clock()

    def main_loop(self):
        while True:
            for event in pg.event.get():
                # if event.type == pg.KEYDOWN:
                #    if event.key == pg.K_ESCAPE:
                #        print("Exiting")
                #        return
                if event.type == pg.QUIT:
                    return
            self.display.fill(C_RED)
            self.draw_background()
            pg.display.flip()
            self.clock.tick(FPS)

    def draw_background(self):
        self.display.blit(self.background, (0, 0))


class Game(Scene):

    def __init__(self, display):
        self.display = pg.display.set_mode(
            (WIDTH, HEIGHT))
        self.space_ship = SpaceShip(
            LATERAL_MARGIN,                         # coord x (left)
            (HEIGHT-LATERAL_MARGIN)/2)              # coord y (top)
        self.clock = pg.time.Clock()
        self.asteroid = Asteroid()
        self.score = Scoreboard()

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
                    print("Ending game")
                    return

            key_status = pg.key.get_pressed()
            if key_status[pg.K_UP]:
                self.space_ship.move(SpaceShip.UP)
            if key_status[pg.K_DOWN]:
                self.space_ship.move(SpaceShip.DOWN)

            if self.score.win == False and self.space_ship.hull_damage.destroyed == False:
                self.asteroid.move()
                self.collide()
            if self.asteroid.x <= 0:
                self.score.add_score()
                self.score.check_win_condition()
                self.asteroid.reset()

            self.display.fill(C_BLACK)
            if not self.space_ship.hull_damage.destroyed:
                pg.draw.rect(self.display, C_WHITE, self.space_ship)
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
                    return
            self.display.fill(C_GREEN)
            pg.display.flip()
