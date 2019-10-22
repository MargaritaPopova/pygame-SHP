import pygame


class Text:
    def __init__(self, string):
        self.font = pygame.font.SysFont('Arial', 29, False)
        self.data = string

    def render_text(self):
        return self.font.render(self.data, 1, (0, 0, 0))