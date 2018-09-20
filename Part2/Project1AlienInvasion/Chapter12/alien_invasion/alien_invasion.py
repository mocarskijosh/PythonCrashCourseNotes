import sys
import pygame


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    # Creates a display window called screen, we draw all of the game's graphical elements on this
    # A screen is called a surface...
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()