import pygame
from pygame.sprite import Sprite

class SmallShip(Sprite):
	"""This is a smaller version of ship image to display as life bar"""
		
	def __init__(self, ai_game):
		"""Spawn and set the starting position of the ship"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()
		self.image = pygame.image.load('images/small_ship.png')
		self.rect =self.image.get_rect()
		