from pygame.locals import *
from guiutils import *
import pygame


monsters = []
spells = []

class gamecontrol:
    """
    This call will control main variables
    of the GUI Screen
    """

    def __init__(self, width, height, name, gamesurface=None):
        self.width = width
        self.height = height
        self.name = name
        self.gamesurface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name)

    def setBackground(self, filepath):
        backimg = pygame.image.load(filepath)
        self.gamesurface.blit(backimg, (self.width-self.width, self.height-self.height))

    def draw(self, guitool):
        guitool.draw(self.gamesurface)
        
    def display(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

            pygame.display.update()

"""
def main(emonsters, espells):

    monsters = emonsters
    spells = espells
    
    pygame.init()
    
    gcontrol = gamecontrol(500, 500, "Yu gi oh Beta")
    gcontrol.setBackground("background.bmp")
    gcontrol.display()
"""        
pygame.init()
    
gcontrol = gamecontrol(1000, 500, "Yu gi oh Beta")
gcontrol.setBackground("gamefiles/background.bmp")

ldbar = ProguessBar(20,20, 50, 10, pygame.Color("white"),pygame.Color("white"))
gcontrol.draw(ldbar)
gcontrol.display()
