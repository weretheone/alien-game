import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    """This is a class for a random star in the background"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()
        # Set a random position within screen size.
        self.rect.x = randint(10,1190)
        self.rect.y = randint(10,790)
