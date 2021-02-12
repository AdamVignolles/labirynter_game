import pygame
import json

class Niveau():
    def __init__(self, minus, all_minus):
        self.minus = minus
        self.all_minus = minus.all_minus
        
        

    def niveau1(self, player):
        self.add_minus( 100, 200 )
        player.rect.x = 100
        player.rect.y = 550
        

    def niveau2(self, player):
        self.add_minus(550, 150 )
        self.add_minus( 100, 200 )
        player.rect.x = 100
        player.rect.y = 550