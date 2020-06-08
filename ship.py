import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""This class defined for the player's ship"""
	
	def __init__(self, ai_game):
		"""Spawn and set the starting position of the ship"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Create a rectangle around the loaded image
		self.image = pygame.image.load('images/ship.png')
		self.rect =self.image.get_rect()

		# Starting position for the ship
		self.rect.midbottom = self.screen_rect.midbottom

		# Store the horizontal position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False


	def blitme(self):
		"""Draw the ship"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""Update the ship's position based on the movement flag and also
		incorporate the ship_speed from settings. This part is also responsible
		to set the boundries where the ship can go."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		elif self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		# 800 does not allow the movement on y axis, change to 0 to allow y axis
		elif self.moving_up and self.rect.top > self.rect.bottom * 0.8:
			self.y -= self.settings.ship_speed
		elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed

		# Update the ship from self.x
		self.rect.x = self.x
		self.rect.y = self.y

	def center_ship(self):
		"""This method is putting back the ship to the center"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

