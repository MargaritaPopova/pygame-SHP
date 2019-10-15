import pygame, sys, random


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


def main():
    pygame.init()
    screen = Screen() # Surface
    ball = Image('basketball.png', screen)
    surface = screen.make_screen() # screen itself
    platform = Platform(screen)
    gameover = False
    d_is_pressed = False # Переменные для постоянного движения платформы при длительном нажатии
    a_is_pressed = False

    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:           #Отследить закрытие окна
                gameover = True
            elif event.type == pygame.VIDEORESIZE:
                surface = screen.resize_screen(event.w, event.h)
            elif event.type == pygame.KEYDOWN:
                if chr(event.key) == 'a':
                    a_is_pressed = True
                elif chr(event.key) == 'd':
                    d_is_pressed = True
            elif event.type == pygame.KEYUP:
                if chr(event.key) == 'a':
                    a_is_pressed = False
                elif chr(event.key) == 'd':
                    d_is_pressed = False
        if d_is_pressed:
            platform.move_right(screen)
        elif a_is_pressed:
            platform.move_left()
        surface.fill(screen.bg_color)           #Обновление окна
        ball.move(screen)
        platform.draw(surface)
        ball.render_image(surface)
        pygame.display.flip()
        pygame.time.wait(90)

    sys.exit(0)


if __name__ == '__main__':
    main()
