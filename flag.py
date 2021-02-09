import pygame

class Flag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("flag.png")
        self.mask_falg = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 110
        self.rect.y = 160
        self.all_flag = pygame.sprite.Group()
    def add_flag(self):
        self.all_flag.add(Flag())

    def start(self, screen):
        self.add_flag()

        self.all_flag.draw(screen)