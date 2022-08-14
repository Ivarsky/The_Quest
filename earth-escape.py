import pygame

SHIP_WIDTH = 20
SHIP_LENGTH = 60
SHIP_COLOR = 255, 255, 255

WIDTH = 1000
HEIGHT = 800
LATERAL_MARGIN = 40


class SpaceShip(pygame.Rect):

    UP = True
    DOWN = False

    def __init__(self, x, y):
        super(SpaceShip, self). __init__(x, y, SHIP_LENGTH, SHIP_WIDTH)
        self.speed = 5

    def move(self, direction):
        if direction == self.UP:
            print("Moving UP")
            self.y = self.y - self.speed
            if self.y < 0:
                self.y = 0
        else:
            print("Moving DOWN")
            self.y = self.y + self.speed
            if self.y > HEIGHT - SHIP_WIDTH:
                self.y = HEIGHT - SHIP_WIDTH


class Asteroid(pygame.Rect):
    def __init__(self):
        super(Asteroid, self).__init__()


class EarthEscape:

    def __init__(self):
        print("Building object EarthEscape")
        pygame.init()
        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.space_ship = SpaceShip(
            LATERAL_MARGIN,                         # coord x (left)
            (HEIGHT-LATERAL_MARGIN)/2)        # coord y (top)

    def main_loop(self):
        print("In main loop")
        while True:
            for event in pygame.event.get():
                # if event.type == pygame.KEYDOWN:
                #    if event.key == pygame.K_ESCAPE:
                #        print("Exiting")
                #        return

                if event.type == pygame.QUIT:
                    print("Exiting")
                    return

            key_status = pygame.key.get_pressed()
            if key_status[pygame.K_UP]:
                self.space_ship.move(SpaceShip.UP)
            if key_status[pygame.K_DOWN]:
                self.space_ship.move(SpaceShip.DOWN)
            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, (SHIP_COLOR), self.space_ship)

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = EarthEscape()
    game.main_loop()
