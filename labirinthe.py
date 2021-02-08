import pygame
from affichage import Affichage
from player import Player

screen = pygame.display.set_mode((720, 700))
pygame.display.set_caption("Labyrinthe")

bg = pygame.image.load("/home/pi/Desktop/python/jeux/labirinthe/bg.png")
bg = pygame.transform.scale(bg, (1800, 1800))
box = pygame.image.load("/home/pi/Desktop/python/jeux/labirinthe/black-check-box.png")
box = pygame.transform.scale(box, (50, 50))
minus = pygame.image.load("/home/pi/Desktop/python/jeux/labirinthe/minus.png")
minus = pygame.transform.scale(minus, (50, 50))
blank = pygame.image.load("/home/pi/Desktop/python/jeux/labirinthe/blank.png")
blank = pygame.transform.scale(blank, (50, 50))
flag = pygame.image.load("/home/pi/Desktop/python/jeux/labirinthe/flag.png")


affichage = Affichage(screen, box, blank)
player = Player()

i = 0
run = True


while run:

    screen.blit(bg, (-250, -350))
    screen.blit(minus, (50,0))
    screen.blit(player.image, player.rect )
    screen.blit(flag, (110, 160))

    Affichage(screen, box, blank)
    


    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not player.rect.y - 50 <= 100:
                    player.move_up()
            elif event.key == pygame.K_DOWN:
                if not player.rect.y + 50 >= 600:
                    player.move_down()
            elif event.key == pygame.K_RIGHT:
                if not player.rect.x + 50 >= 600:
                    player.move_right()
            elif event.key == pygame.K_LEFT:
                if not player.rect.x + 50 <= 150:
                    player.move_left()

 