import pygame
import time
from flag import Flag
from minus import Minus
import json

pygame.init()

flag = Flag()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.flag = flag
        self.win = False
        self.image = pygame.image.load("fitness-ball.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.mask_player = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.font = pygame.font.Font("/home/pi/Desktop/python/jeux/labirynter_game/NotoSerif-Regular.ttf", 25)
        self.rect.x = 100
        self.rect.y = 550
        self.velocity = 50

    def Win(self, screen):
        self.minus = Minus()
        if self.win == True:
            score_text = self.font.render("WIN", True, (0, 0, 0))
            screen.blit(score_text, (20, 20))
            self.minus.start(screen, Player(), 2)
            with open('level.json', 'r')as infile:
                level= json.load(infile)
                niveau = level
            del level
            with open('level.json', 'w') as outfile:
                niveau += 1
                json.dump(niveau, outfile)
            print(niveau)
            

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def move_right(self, screen):
        self.rect.x += self.velocity
            
    def move_left(self, screen):
        self.rect.x -= self.velocity
           
    def move_up(self, screen):
        self.rect.y -= self.velocity
      
    def move_down(self, screen):
        self.rect.y += self.velocity