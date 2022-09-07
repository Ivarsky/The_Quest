import pygame as pg

from the_quest import *
from the_quest.scenes import Front, Game, HallOfFame

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

        self.scenes = [
            Front(self.display),
            Game(self.display),
            HallOfFame(self.display),
        ]

    def play(self):
        print("Game open")

        for scene in self.scenes:
            scene.main_loop()


if __name__ == "__main__":
    game = TheQuest()
    game.play()
