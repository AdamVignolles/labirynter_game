import pygame
import json
from niveau import Niveau

class Minus(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load("minus.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.mask_minus = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.all_minus = pygame.sprite.Group()
        

    def add_minus(self, x, y):
        self.all_minus.add(Minus(x, y))

    def start(self, screen, player, niveau=1):

        with open('level.json', 'r')as infile:
            level= json.load(infile)


        if level == 1:
            Niveau.niveau1(self, player)
        elif level == 2:
            Niveau.niveau2(self, player)
            

        self.all_minus.draw(screen)