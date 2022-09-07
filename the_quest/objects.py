import pygame as pg

from the_quest import *

from random import randint


class HullPoints:
    """
    Guarda los puntos de vida de la nave y los pinta
    """

    def __init__(self):
        self.initialize()
        pg.font.init()
        self.typography = pg.font.SysFont('urwbookman', 50)
        self.typography_endgame = pg.font.SysFont('urwbookman', 100)

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


class SpaceShip(pg.Rect):

    UP = True
    DOWN = False

    hull_damage = HullPoints()

    def __init__(self, x, y):
        super(SpaceShip, self). __init__(x, y, SHIP_LENGTH, SHIP_WIDTH)
        self.speed = 5

    def move(self, direction):
        """
        Mueve la nave arriba o abajo según que tecla se pulse
        """

        if direction == self.UP:
            self.y = self.y - self.speed
            if self.y < 0:
                self.y = 0
        else:
            self.y = self.y + self.speed
            if self.y > HEIGHT - SHIP_WIDTH:
                self.y = HEIGHT - SHIP_WIDTH

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
        self.typography = pg.font.SysFont('urwbookman', 50)
        self.typography_endgame = pg.font.SysFont('urwbookman', 100)

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
