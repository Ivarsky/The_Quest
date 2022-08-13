import pygame


class SpaceShip(pygame.Rect):
    pass


class EarthEscape:

    _WIDTH = 1000
    _HEIGHT = 800
    _LATERAL_MARGIN = 40

    _SHIP_HEIGHT = 10
    _SHIP_WIDTH = 40
    _SHIP_COLOR = 255, 255, 255

    def __init__(self):
        print("building object EarthEscape")
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self._WIDTH, self._HEIGHT))

        self.space_ship = SpaceShip(
            self._LATERAL_MARGIN,       # coord x (left)
            (self._HEIGHT-40)/2,        # coord y (top)
            self._SHIP_WIDTH,           # width
            self._SHIP_HEIGHT)          # height

    def main_loop(self):
        print("in main loop")
        while True:
            for event in pygame.event.get():
                # if event.type == pygame.KEYDOWN:
                #    if event.key == pygame.K_ESCAPE:
                #        print("Exit")
                #        return
                if event.type == pygame.QUIT:
                    print("Exit")
                    return
            pygame.draw.rect(self.screen, (self._SHIP_COLOR), self.space_ship)
            pygame.display.flip()


if __name__ == "__main__":
    game = EarthEscape()
    game.main_loop()
