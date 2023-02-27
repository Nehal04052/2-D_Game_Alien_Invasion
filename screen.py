import sys
import pygame

class Ai:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((720,720))
        
    def run_game(self):
         while True:
            if event.type== pygame.event.Quit:
                sys.exit()
            
if __name__=='__main__':
    a = Ai()
    a.run_game()
