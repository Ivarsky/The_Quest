from random import randint
import pygame


class TheQuest:

    score = Scoreboard()

    def __init__(self):
        print("Building object EarthEscape")
        pygame.init()
        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        # Preparacion para pintar texto

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
            if not self.space_ship.hull_damage.destroyed:
                self.asteroid.reset()

    def main_loop(self):
        print("In main loop")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #    if event.key == pygame.K_ESCAPE:
                    #        print("Exiting")
                    #        return
                    if event.key == pygame.K_r:
                        self.score.initialize()
                        self.space_ship.hull_damage.initialize()

                if event.type == pygame.QUIT:
                    print("Exiting")
                    return

            key_status = pygame.key.get_pressed()
            if key_status[pygame.K_UP]:
                self.space_ship.move(SpaceShip.UP)
            if key_status[pygame.K_DOWN]:
                self.space_ship.move(SpaceShip.DOWN)

            if self.score.win == False and self.space_ship.hull_damage.destroyed == False:
                self.asteroid.move()
                self.collide()
            if self.asteroid.x <= 0:
                self.score.add_score()
                self.score.check_win_condition()
                self.asteroid.reset()

            self.screen.fill(C_BLACK)
            if not self.space_ship.hull_damage.destroyed:
                pygame.draw.rect(self.screen, C_WHITE, self.space_ship)
            pygame.draw.rect(self.screen, C_WHITE, self.asteroid)
            # dibuja los puntos para ganar (asteroides esquivados)
            self.score.draw(self.screen)
            # dibuja los puntos para perder (golpes a la nave)
            self.space_ship.hull_damage.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    TheQuest()
