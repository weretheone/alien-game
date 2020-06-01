import pygame

class Ship:
	"""This class defined for the player's ship"""
	
	def __init__(self, ai_game):
		"""Spawn and set the starting position of the ship"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# Create a rectangle around the loaded image
		self.image = pygame.image.load('images/ship.bmp')
		self.rect =self.image.get_rect()

		# Starting position for the ship
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		"""Draw the ship"""
		self.screen.blit(self.image, self.rect)