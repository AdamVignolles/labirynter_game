import pygame

class Player():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/home/pi/Desktop/python/jeux/labirinthe/fitness-ball.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 550
        self.velocity = 50

    def move_right(self):
        self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity
    def move_up(self):
        self.rect.y -= self.velocity
    def move_down(self):
        self.rect.y += self.velocity

