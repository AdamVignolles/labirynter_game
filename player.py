import pygame
from flag import Flag

pygame.init()

flag = Flag()

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.flag = flag
        self.win = False
        self.screen = screen
        self.image = pygame.image.load("fitness-ball.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
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
        return self.rect.colliderect(sprite.rect)

    def move_right(self):
        if not self.check_collision(self.flag):
            self.win = True
        self.rect.x += self.velocity
    def move_left(self):
        if not self.check_collision(self.flag):
            self.win = True
        self.rect.x -= self.velocity
    def move_up(self):
        if not self.check_collision(self.flag):
            self.win = True
        self.rect.y -= self.velocity 
    def move_down(self):
        if not self.check_collision(self.flag):
            self.win = True
        self.rect.y += self.velocity

