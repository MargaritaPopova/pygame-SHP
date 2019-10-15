import pygame


class Screen:

    def __init__(self):
        self.width = 400
        self.height = 300
        self.size = self.width, self.height
        self.bg_color = 255, 255, 240

    def make_screen(self):
        return pygame.display.set_mode(self.size, pygame.RESIZABLE)

    def resize_screen(self, x, y):
        self.width, self.height = x, y
        self.size = [self.width, self.height]
        return self.make_screen()