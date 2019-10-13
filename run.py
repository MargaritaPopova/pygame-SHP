import pygame, sys, random

WIDTH = 800
HEIGHT = 600


class Screen:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.size = self.width, self.height
        self.bg_color = 255, 240, 245

    def make_screen(self):
        screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        return screen

    def resize_screen(self, event):
        width = event.w
        height = event.h
        size = [width, height]
        return pygame.display.set_mode(size, pygame.RESIZABLE)


class Image:

    def __init__(self, filename):

        self.image_load = pygame.image.load(filename)
        self.image_rect = self.image_load.get_rect()
        self.image_rect.x = WIDTH//2
        self.image_rect.y = HEIGHT//2
        self.step_x = random.randint(10, 50)
        self.step_y = random.randint(10, 50)

    def render_image(self, screen):
        screen.blit(self.image_load, self.image_rect)

    def move(self):
        if (self.image_rect.x + 100) > WIDTH or self.image_rect.x < 0:
            self.step_x *= -1

        if (self.image_rect.y + 100) > HEIGHT or self.image_rect.y < 0:
            self.step_y *= -1

        self.image_rect.x += self.step_x
        self.image_rect.y += self.step_y


class Platform:

    def __init__(self):
        self.width = 200
        self.height = 30
        self.color = 85, 107, 47
        self.x = 100
        self.y = 500

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

    def move_left(self):
        if self.x <= 0:
            self.x = 0
        else:
            self.x -= 50

    def move_right(self):
        if self.x + self.width >= WIDTH:
            self.x = WIDTH - self.width
        else:
            self.x += 50


def main():
    pygame.init()
    sc = Screen() # Surface
    ball = Image('basketball.png')
    screen = sc.make_screen() # screen itself
    platform = Platform()
    gameover = False
    d_is_pressed = False # Переменные для постоянного движения платформы при длительном нажатии
    a_is_pressed = False

    while not gameover:
        screen.fill(sc.bg_color)           #Обновление окна
        for event in pygame.event.get():   #Отследить закрытие окна
            if event.type == pygame.QUIT:
                gameover = True
            elif event.type == pygame.VIDEORESIZE:
                screen = sc.resize_screen(event)
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
            platform.move_right()
        elif a_is_pressed:
            platform.move_left()
        ball.move()
        platform.draw(screen)
        ball.render_image(screen)
        pygame.display.flip()
        pygame.time.wait(90)

    sys.exit(0)


if __name__ == '__main__':
    main()
