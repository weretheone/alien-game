import sys
import pygame

# Load the Settings, Ship, Bullet class from separate files
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """This is the base game class which manages the assets and behaviours"""
    
    def __init__(self):
        """Init the game with base game resources, set the display name & size"""
        # Create an instance and assign the settings.
        pygame.init()
        self.settings = Settings()
        # Set the icon and name for the window
        pygame.display.set_icon(self.settings.game_icon)
        pygame.display.set_caption(self.settings.game_name)
        # Init the screen in windowed mode.
        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        # Disable the visibility of the mouse on the game screen
        pygame.mouse.set_visible(0)
        # Init the ship.
        self.ship = Ship(self)
        # Init the bullet sprite.
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """This is the main loop for the game"""
        while True:
            # Checking for events during each loop.
            self._check_events()
            # Update the ship based on events
            self.ship.update()
            # Update the bullet
            self.bullets.update()
            # Remove the bullets which are not visible
            self._update_bullet() 
            # Update the screen
            self._update_screen()
   

    def _check_events(self):
        """This method is for collecting the user events"""
        for event in pygame.event.get():
            # Event for exit
            if event.type == pygame.QUIT:
                sys.exit()
            # Key pressed
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Key released
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """This method is responsible to check and react to key press"""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left.
            self.ship.moving_left = True 
        elif event.key == pygame.K_UP:
            # Move the ship up.
            self.ship.moving_up = True 
        elif event.key == pygame.K_DOWN:
            # Move the ship down.
            self.ship.moving_down = True 
        elif event.key == pygame.K_q:
            # Exit the game on 'q'
            sys.exit()
        elif event.key == pygame.K_SPACE:
            # Move the ship down.
            self._fire_bullet() 

    def _check_keyup_events(self, event):
        """This method is responsible to check and react to key release, some
        specific things like movement of the ship should react once key no
        longer pressed down."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        """This method is for the screen handling, all visible items should 
        included in this method to display on the screen."""
        # Set the background color during each redraw.
        self.screen.fill(self.settings.bg_color)
        # Draw the group of bullets on the screen.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Draw the ship after bullets so it is above the bullet
        self.ship.blitme()
        # Display the most recently drawn screen visible
        pygame.display.flip()

    def _fire_bullet(self):
        """This method will call the Bullet method for a new bullet then it
         will add it to the group we defined earlier. """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        """This method is responsible to remove the bullets which are no longer
        visible on the screen."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
               self.bullets.remove(bullet)


if __name__ == '__main__':
    # Create an instance from the above class and launch it.
    ai = AlienInvasion()
    ai.run_game()