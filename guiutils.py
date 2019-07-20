import pygame
from pygame.locals import *


class GuiTool(object):
    def __init__(self, posx=0, posy=0, width=0, height=0, color=pygame.Color("white")):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.color = color

    def position(self):
        return posx,posy
    
    
class ProguessBar(GuiTool):

    def __init__(self, posx=0, posy=0, width=0, height=0, color=pygame.Color("white"), color2=pygame.Color("black")):
        self.color2 = color2
        self.percentage = 0
        super(ProguessBar, self).__init__(posx, posy, width, height, color)

    def draw(self, surface):
        loadingbar = pygame.Rect(self.posx, self.posy, self.width, self.height)
        #surface.fill(self.color, loadingbar)
        #surface.blit(surface, loadingbar)
