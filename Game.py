from Image import Image
from Platform import Platform
from Screen import Screen


class Game:

    def __init__(self):
        self.screen = Screen()
        self.ball = Image('basketball.png', self.screen)
        self.surface = self.screen.make_screen()  # screen itself
        self.platform = Platform(self.screen)
        self.game_over = False

        self.buttons = {
            'd_is_pressed': False,  # Переменные для постоянного движения платформы при длительном нажатии
            'a_is_pressed': False
        }

    def move_platform(self):
        if self.buttons['d_is_pressed']:
            self.platform.move_right(self.screen)
        elif self.buttons['a_is_pressed']:
            self.platform.move_left()

    def run(self):
        self.surface.fill(self.screen.bg_color)
        self.move_platform()
        self.ball.move(self.screen)
        self.platform.draw(self.surface)
        self.ball.render_image(self.surface)