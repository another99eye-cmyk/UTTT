import pygame
from game import Game

WIDTH, HEIGHT = 900, 900
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ultimate Tic-Tac-Toe")
    clock = pygame.time.Clock()

    game = Game(screen, WIDTH, HEIGHT)

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                game.handle_event(event)

        game.update(dt)
        game.draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()