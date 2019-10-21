import pygame
from random import randint


class Platform:

    def __init__(self, screen):
        self.width = screen.width//4
        self.height = 10
        self.color = 85, 107, 47
        self.x = randint(0, screen.width)
        self.y = randint(0, screen.height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def recalculate_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def collides_with(self, ball):
        return self.rect.colliderect(ball.image_rect)

    def move_left(self):
        if self.x <= 0:
            self.x = 0
        else:
            self.x -= 50
        self.recalculate_rect()

    def move_right(self, screen):
        if self.x + self.width >= screen.width:
            self.x = screen.width - self.width
        else:
            self.x += 50
        self.recalculate_rect()

