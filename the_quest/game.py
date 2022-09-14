import os

import pygame as pg

from random import randint

from . import *
from .scenes import Front, Game1, Game2, HallOfFame, Story, Story2


class TheQuest:

    def __init__(self):
        print("Building object EarthEscape")
        pg.init()
        self.display = pg.display.set_mode(
            (WIDTH, HEIGHT))
        pg.display.set_caption("The Quest BZ Ivan version")
        icon = pg.image.load(os.path.join(
            "resources", "player", "sprites", "player1.png"))
        pg.display.set_icon(icon)

        self.scenes = [
            Front(self.display),
            Story(self.display),
            Game1(self.display),
            Story2(self.display),
            Game2(self.display),
            HallOfFame(self.display),
        ]

    def play(self):
        print("Game open")

        for scene in self.scenes:
            scene.main_loop()


if __name__ == "__main__":
    game = TheQuest()
    game.play()
