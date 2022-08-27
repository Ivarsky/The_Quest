from random import randint
import pygame

WIDTH = 1000
HEIGHT = 800

SHIP_WIDTH = 20
SHIP_LENGTH = 60
LATERAL_MARGIN = 40
MAX_HULL_HITPOINTS = 3

ASTEROID_SIZE = 25
ASTEROID_SPEED = 7

C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)

WIN_SCORE = 3


class HullPoints:
    """
    Guarda los puntos de vida de la nave y los pinta
    """

    def __init__(self):
        self.initialize()

    def ckeck_gameover_condition(self):
        if self.points == MAX_HULL_HITPOINTS:
            print("Ship Destroyed!, GAME OVER")
            self.gameover = True
        else:
            print(
                f"Collision! {MAX_HULL_HITPOINTS - self.points} hull points left!")

    def initialize(self):
        self.points = 0
        self.gameover = False


class SpaceShip(pygame.Rect):

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


class Asteroid(pygame.Rect):
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


class EarthEscape:

    score = Scoreboard()

    def __init__(self):
        print("Building object EarthEscape")
        pygame.init()
        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.space_ship = SpaceShip(
            LATERAL_MARGIN,                         # coord x (left)
            (HEIGHT-LATERAL_MARGIN)/2)              # coord y (top)

        self.asteroid = Asteroid()

    def collide(self):
        """
        Comprueba si el asteroide colisiona con la nave, resetea la posición del asteroide y resta un punto de vida
        """
        if pygame.Rect.colliderect(self.asteroid, self.space_ship):
            self.space_ship.hit_hull()
            self.space_ship.hull_damage.ckeck_gameover_condition()
            if not self.space_ship.hull_damage.gameover:
                self.asteroid.reset()

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
            self.screen.fill(C_BLACK)
            if self.score.win == False and self.space_ship.hull_damage.gameover == False:
                self.asteroid.move()
                self.collide()
            if self.asteroid.x <= 0:
                self.score.add_score()
                self.score.check_win_condition()
                self.asteroid.reset()
            if not self.space_ship.hull_damage.gameover:
                pygame.draw.rect(self.screen, C_WHITE, self.space_ship)
            pygame.draw.rect(self.screen, C_WHITE, self.asteroid)

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = EarthEscape()
    game.main_loop()
