import pygame

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        # Game settings
        self.game_name = 'Alien Invasion - weretheone'
        self.game_icon = pygame.image.load('images/icon.png')
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (64, 185, 126)

        # Ship settings
        self.ship_speed = 1.4

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 1, 1)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 0.4
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1