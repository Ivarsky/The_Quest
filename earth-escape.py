import pygame


class EarthEscape:

    _ALTO = 200
    _ANCHO = 320

    def __init__(self):
        print("contruyendo un objeto EarthEscape")
        pygame.init()
        self.pantalla = pygame.display.set_mode((self._ANCHO, self._ALTO))

    def bucle_principal(self):
        print("estoy en el bucle principal")
        while True:
            pygame.display.flip()


if __name__ == "__main__":
    juego = EarthEscape()
    juego.bucle_principal()
