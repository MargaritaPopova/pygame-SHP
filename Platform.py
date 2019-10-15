import pygame


class Platform:

    def __init__(self, screen):
        self.width = screen.width//4
        self.height = 10
        self.color = 85, 107, 47
        self.x = 0
        self.y = screen.height - self.height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

    def move_left(self):
        if self.x <= 0:
            self.x = 0
        else:
            self.x -= 50

    def move_right(self, screen):
        if self.x + self.width >= screen.width:
            self.x = screen.width - self.width
        else:
            self.x += 50