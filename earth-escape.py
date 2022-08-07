import pygame


class EarthEscape:

    _HEIGHT = 200
    _WIDTH = 320

    def __init__(self):
        print("building object EarthEscape")
        pygame.init()
        self.screen = pygame.display.set_mode((self._WIDTH, self._HEIGHT))

    def main_loop(self):
        print("in main loop")
        triangle_ship = [[10, 20], [10, 30], [30, 25]]
        while True:
            pygame.draw.polygon(self.screen, (255, 255, 255), triangle_ship)
            pygame.display.flip()


if __name__ == "__main__":
    game = EarthEscape()
    game.main_loop()
