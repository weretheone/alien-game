import sys
import pygame

# Load the Settings & Ship class from separate files
from settings import Settings
from ship import Ship

class AlienInvasion:
    """This is the base game class which manages the assets and behaviours"""
    
    def __init__(self):
        """Init the game with base game resources, set the display name & size"""
        pygame.init()
        pygame.display.set_caption('Alien Invasion - weretheone')
        program_icon = pygame.image.load('images/alien.png')
        pygame.display.set_icon(program_icon)
        # Create an instance and assign to the settings.
        self.settings = Settings()
        # Init the screen
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # Init the ship
        self.ship = Ship(self)

    def run_game(self):
        """This is the main loop for the game"""
        while True:
            # Checking for events during each loop.
            self._check_events()
            # Update the screen
            self._update_screen()
            
    def _check_events(self):
        """This method is for collecting the user events"""
        # exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.
                    self.ship.rect.x += 1

    def _update_screen(self):
        """This method is for the screen handling"""
        # Set the background color during each redraw.
        self.screen.fill(self.settings.bg_color)
        # Draw the ship
        self.ship.blitme()
        # Display the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Create an instance from the above class and launch it.
    ai = AlienInvasion()
    ai.run_game()