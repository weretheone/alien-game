import sys
import pygame
from time import sleep

# Load the classes from separate files
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """This is the base game class which manages the assets and behaviours"""
    
    def __init__(self):
        """Init the game with base game resources, set the display name  and
         size and do various settings"""
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
        #pygame.mouse.set_visible(0)
        #Init the statistics
        self.stats = GameStats(self)
        # Init the ship.
        self.ship = Ship(self)
        # Init the bullet sprite.
        self.bullets = pygame.sprite.Group()
        # Init the aliens.
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # Init the stars
        self.stars = pygame.sprite.Group()
        self._create_stars()
        # Init the scoreboard
        self.sb = Scoreboard(self)
        # Init the start button
        self.play_button = Button(self, "Start")

    def run_game(self):
        """This is the main loop for the game"""
        while True:
            # Checking for events during each loop.
            self._check_events()
            # Call the main loop only when the game active
            if self.stats.game_active:
                # Update the ship based on events
                self.ship.update()
                # Update the bullet
                self.bullets.update()
                # Update the aliens
                self._update_aliens()
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
            # Clicking the mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
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
        elif event.key == pygame.K_SPACE and self.stats.game_active:
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
        # Fill the background with some stars
        self.stars.draw(self.screen)
        # Draw the group of bullets on the screen.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Draw the alien fleet
        self.aliens.draw(self.screen)
        # Draw the ship after bullets so it is above the bullet
        self.ship.blitme()
        # Draw the Start button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()
        # Draw the scroeboard
        self.sb.show_score()
        # Display the most recently drawn screen visible
        pygame.display.flip()


    def _create_stars(self):
        """This method is for creating stars in the background"""
        # Fill the background with 50 stars
        for each_star in range(60):
            star = Star(self)
            self.stars.add(star)

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
            if bullet.rect.bottom <= 0:
               self.bullets.remove(bullet)
        # Check for any bullets that have hit aliens.
        self._check_bullet_alien_colission()
        # Check if any alien remain after bullet hit
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _check_bullet_alien_colission(self):
        """This method checks if any bullet and alien sprite collided and if so
         then it will remove both the alien and the bullet."""
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        # It will update the score on each hit
        if collisions:
            for alien in collisions.values():
                self.stats.score += self.settings.alien_points * len(alien)
            self.sb.prep_score()
            # Higscore check
            self.sb.check_high_score()

    def _update_aliens(self):
        """This method is for moving aliens around the screen and update their
        position based on the speed"""
        self._check_fleet_edges()
        self.aliens.update()
        # Check if any alien hit the player's ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # Check if any alien reached the bottom
        self._check_aliens_bottom()

    def _create_fleet(self):
        """This method is for creating the alien fleet above the player"""
        alien = Alien(self)
        # Examine the alien image size
        alien_width, alien_height = alien.rect.size
        # Add some space at the two end as margin
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # Find out how many aliens fit in one row
        number_aliens_x = available_space_x // (2 * alien_width)
        # Examine the ship height and add in the calculations
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                                (3 * alien_height) - ship_height)
        # Find out how many rows fit
        numer_rows = available_space_y // (2 * alien_height)
        # Create the aliens
        for row_number in range(numer_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
       
    def _create_alien(self, alien_number, row_number):
        """Create the aliens on the screen""" 
        alien = Alien(self)
        alien_width, alien.height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number 
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond to alien reaching edge of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break 

    def _change_fleet_direction(self):
        """Drop the entire fleet and change it's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """This is the method we call when a ship is hit by an alien"""
        # Decrement ships_left.
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.sb.ships.draw(self.screen)
            # Reveal the mouse
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game stats
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            # Hide the mouse
            pygame.mouse.set_visible(False)
            # Reset the score
            self.sb.prep_score()
            # Reset the life count
            self.sb.prep_ships()
            # Start the game 
            self.stats.game_active = True


if __name__ == '__main__':
    # Create an instance from the game class and launch it.
    ai = AlienInvasion()
    ai.run_game()