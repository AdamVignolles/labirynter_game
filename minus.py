import pygame

class Minus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("minus.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.mask_minus = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 200
        self.all_minus = pygame.sprite.Group()
    def add_minus(self):
        self.all_minus.add(Minus())

    def start(self, screen):
        self.add_minus()

        self.all_minus.draw(screen)