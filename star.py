import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    """This is a class for a random star in the background"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()
        # Set a random position within screen size.
        self.rect.x = randint(10, self.settings.screen_width - 10)
        self.rect.y = randint(10, self.settings.screen_height - 10)
