import pygame

class brick():
    def __init__(self, pos_x, pos_y, image_ruta):
        self.__image = pygame.image.load(image_ruta)
        self.__rect = self.image.get_rect()
        self.__rect.move_ip(pos_x, pos_y)

    @property
    def rect(self):
        return self.__rect

    @property
    def image(self):
        return self.__image

    def move(self, posi_x, posi_y):
        self.__rect.move(posi_x, posi_y)

class irrompible(brick):
    pass

