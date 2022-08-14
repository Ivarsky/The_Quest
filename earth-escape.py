from curses import KEY_DOWN
import pygame

SHIP_HEIGHT = 10
SHIP_WIDTH = 40


class SpaceShip(pygame.Rect):

    UP = True
    DOWN = False

    def __init__(self, x, y):
        super(SpaceShip, self). __init__(x, y, SHIP_WIDTH, SHIP_HEIGHT)
        self.velocidad = 5

    def move(self, direction):
        if direction == self.UP:
            print("Moving UP")
        else:
            print("Moving DOWN")


class EarthEscape:

    _WIDTH = 1000
    _HEIGHT = 800
    _LATERAL_MARGIN = 40

    _SHIP_COLOR = 255, 255, 255

    def __init__(self):
        print("Building object EarthEscape")
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self._WIDTH, self._HEIGHT))

        self.space_ship = SpaceShip(
            self._LATERAL_MARGIN,                         # coord x (left)
            (self._HEIGHT-self._LATERAL_MARGIN)/2)        # coord y (top)

    def main_loop(self):
        print("In main loop")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.space_ship.move(SpaceShip.UP)
                    elif event.key == pygame.K_DOWN:
                        self.space_ship.move(SpaceShip.DOWN)

                #    elif event.key == pygame.K_ESCAPE:
                #        print("Exiting")
                #        return

                if event.type == pygame.QUIT:
                    print("Exiting")
                    return
            pygame.draw.rect(self.screen, (self._SHIP_COLOR), self.space_ship)
            pygame.display.flip()


if __name__ == "__main__":
    game = EarthEscape()
    game.main_loop()
