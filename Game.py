from Image import Image
from Platform import Platform
from Screen import Screen
from Text import Text


class Game:
    filename = 'basketball.png'

    def __init__(self):
        self.screen = Screen()
        self.surface = self.screen.make_screen()  # screen itself
        self.platform = Platform(self.screen)
        self.game_over = False
        self.objects = []
        self.ball = Image(self.filename)
        self.game_over_text = Text("Game over!")

        self.buttons = {
            'd_is_pressed': False,  # Переменные для постоянного движения платформы при длительном нажатии
            'a_is_pressed': False
        }

    def make_multiple_objects(self, amount):
        for i in range(amount):
            self.objects.append(Image(self.filename))

    def move_platform(self):
        if self.buttons['d_is_pressed']:
            self.platform.move_right(self.screen)
        elif self.buttons['a_is_pressed']:
            self.platform.move_left()

    def process_collisions(self):
        if self.platform.collides_with(self.ball):
            self.ball.collision()

    def run_multiple(self):
        for ball in self.objects:
            ball.move(self.screen)
            ball.render_image(self.surface)

    def game_is_over(self):
        self.surface.blit(self.game_over_text.render_text(), (50, 100))

    def run(self):
        self.surface.fill(self.screen.bg_color)
        self.move_platform()
        self.platform.draw(self.surface)
        # self.run_multiple()
        self.ball.move(self.screen)
        self.ball.render_image(self.surface)
        self.process_collisions()
        if self.ball.touches_bottom(self.screen):
            self.game_is_over()









