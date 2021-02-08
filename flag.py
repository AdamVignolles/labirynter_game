import pygame

class Flag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("flag.png")
        self.rect = self.image.get_rect()
        self.rect.x = 110
        self.rect.y = 160