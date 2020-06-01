import sys
import pygame

#Load the Settings class from the settings.py file
from settings import Settings

class AlienInvasion:
    """This is the base game class which manages the assets and behaviours"""
    
    def __init__(self):
        """Init the game with base game resources, set the display name & size"""
        pygame.init()
        pygame.display.set_caption('Alien Invasion - weretheone')
        program_icon = pygame.image.load('images/alien.png')
        pygame.display.set_icon(program_icon)
        #Create an instance and assign to the settings
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
    def run_game(self):
        """This is the main loop for the game"""
        while True:
            #Checking for events during each loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Set the color during each redraw 
            self.screen.fill(self.settings.bg_color)
            #Display the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # Create an instance from the above class and launch it
    ai = AlienInvasion()
    ai.run_game()