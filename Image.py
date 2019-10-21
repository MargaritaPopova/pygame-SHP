import pygame
from random import randint


class Image:

    def __init__(self, filename):

        self.image_load = pygame.image.load(filename)
        self.image_rect = self.image_load.get_rect()
        self.image_rect.x = randint(10, 100)
        self.image_rect.y = randint(10, 100)
        self.step_x = randint(10, 20)
        self.step_y = randint(10, 30)

    def render_image(self, screen):
        screen.blit(self.image_load, self.image_rect)

    def move(self, screen):
        self.image_rect.x += self.step_x
        self.image_rect.y += self.step_y

        if (self.image_rect.x + 100) > screen.width or self.image_rect.x < 0:
            self.step_x *= -1
        if (self.image_rect.y + 100) > screen.height or self.image_rect.y < 0:
            self.step_y *= -1

    def collision(self):
        self.step_x *= -1
        self.step_y *= -1
