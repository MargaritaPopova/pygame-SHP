import pygame, sys
from Game import Game


def run_event_listener(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Отследить закрытие окна
            game.game_over = True
        elif event.type == pygame.VIDEORESIZE:
            game.surface = game.screen.resize_screen(event.w, event.h)
        elif event.type == pygame.KEYDOWN:
            if chr(event.key) == 'a':
                game.buttons['a_is_pressed'] = True
            elif chr(event.key) == 'd':
                game.buttons['d_is_pressed'] = True
        elif event.type == pygame.KEYUP:
            if chr(event.key) == 'a':
                game.buttons['a_is_pressed'] = False
            elif chr(event.key) == 'd':
                game.buttons['d_is_pressed'] = False


def main():
    pygame.init()
    game = Game()

    while not game.game_over:
        run_event_listener(game)
        game.run()           # Запуск игры
        pygame.display.flip()
        pygame.time.wait(100)

    sys.exit(0)


if __name__ == '__main__':
    main()
