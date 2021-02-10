import pygame
from flag import Flag
from minus import Minus

pygame.init()

flag = Flag()


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.flag = flag
        self.minus = Minus()
        self.win = False
        self.screen = screen
        self.image = pygame.image.load("fitness-ball.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.mask_player = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.font = pygame.font.Font("/home/pi/Desktop/python/jeux/labirynter_game/NotoSerif-Regular.ttf", 25)
        self.rect.x = 100
        self.rect.y = 550
        self.velocity = 50

    def Win(self):
        if self.win == True:
            score_text = self.font.render("WIN", True, (0, 0, 0))
            self.screen.blit(score_text, (20, 20))

    def check_collision(self, sprite):
        return pygame.sprite.spritecollide(sprite, False)


    def move_right(self):
        self.rect.x += self.velocity
        if not self.rect.colliderect(self.minus):
            if self.rect.colliderect(self.flag):
                self.win = True
                self.Win()
            else:
                self.win = False
        else:
            self.move_left()
            
        
    def move_left(self):
        self.rect.x -= self.velocity
        if  not self.rect.colliderect(self.minus):
            if self.rect.colliderect(self.flag):
                self.win = True
                self.Win()
            else:
                self.win = False
        else:
            self.move_right()
           
        
    def move_up(self):
        self.rect.y -= self.velocity
        if not self.rect.colliderect(self.minus):
            if self.rect.colliderect(self.flag):
                self.win = True
                self.Win()
            else:
                self.win = False
        else:
            self.rect.y += self.velocity * 2
                
            
                
                

    def move_down(self):
        self.rect.y += self.velocity
        if  not self.rect.colliderect(self.minus):
            if self.rect.colliderect(self.flag):
                self.win = True
                self.Win()
            else:
                self.win = False
        else:
            self.move_up()
