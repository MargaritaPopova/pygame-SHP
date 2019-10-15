import random, pygame


class Image:

    def __init__(self, filename, screen):

        self.image_load = pygame.image.load(filename)
        self.image_rect = self.image_load.get_rect()
        self.image_rect.x = screen.width//2
        self.image_rect.y = screen.height//2
        self.step_x = random.randint(10, 50)
        self.step_y = random.randint(10, 50)

    def render_image(self, screen):
        screen.blit(self.image_load, self.image_rect)

    def move(self, screen):
        if (self.image_rect.x + 100) > screen.width or self.image_rect.x < 0:
            self.step_x *= -1

        if (self.image_rect.y + 100) > screen.height or self.image_rect.y < 0:
            self.step_y *= -1

        self.image_rect.x += self.step_x
        self.image_rect.y += self.step_y