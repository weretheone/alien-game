import pygame

class Ship:
	"""This class defined for the player's ship"""
	
	def __init__(self, ai_game):
		"""Spawn and set the starting position of the ship"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
