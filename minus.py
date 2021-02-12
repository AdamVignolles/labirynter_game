import pygame

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

    def start(self, screen):
        self.add_minus(250, 150 )
        self.add_minus( 300, 550 )

        self.all_minus.draw(screen)