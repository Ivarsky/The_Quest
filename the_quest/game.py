import pygame as pg

from the_quest import *
from the_quest.scenes import Front, Game, HallOfFame
from the_quest.objects import Asteroid, Scoreboard, SpaceShip

from random import randint


class TheQuest:

    def __init__(self):
        print("Building object EarthEscape")
        pg.init()
        self.display = pg.display.set_mode(
            (WIDTH, HEIGHT))
        pg.display.set_caption("The Quest BZ Ivan version")
        icon = pg.image.load("resources/player/sprites/player1.png")
        pg.display.set_icon(icon)

        self.clock = pg.time.Clock()

        self.space_ship = SpaceShip(
            LATERAL_MARGIN,                         # coord x (left)
            (HEIGHT-LATERAL_MARGIN)/2)              # coord y (top)

        self.asteroid = Asteroid()
        self.score = Scoreboard()

        self.scenes = [
            Front(self.display),
            Game(self.display),
            HallOfFame(self.display),
        ]

    def collide(self):
        """
        Comprueba si el asteroide colisiona con la nave, resetea la posición del asteroide y resta un punto de vida
        """
        if pg.Rect.colliderect(self.asteroid, self.space_ship):
            self.space_ship.hit_hull()
            self.space_ship.hull_damage.ckeck_gameover_condition()
            if not self.space_ship.hull_damage.destroyed:
                self.asteroid.reset()

    def play(self):
        print("In main loop")

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
            self.clock.tick(60)


if __name__ == "__main__":
    game = TheQuest()
    game.play()
