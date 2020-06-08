import pygame

class Settings:
    """A class to store constant and dynamic settings for Alien Invasion."""

    def __init__(self):
        """The basic init holds the constant settings"""
        # Game settings
        self.game_name = 'Alien Invasion - weretheone'
        self.game_icon = pygame.image.load('images/icon.png')
        
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (64, 185, 126)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 1, 1)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 10

        # Game mechanics
        self.speedup_scale = 1.2
        self.score_scale = 1.2
        self. initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings which change during the game"""
        self.ship_speed = 1.4
        self.bullet_speed = 1.5
        self.alien_speed = 0.4
        self.alien_points = 50

        # Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """This method increase the speed of the game and alien point value"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)