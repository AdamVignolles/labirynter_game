import pygame
from affichage import Affichage
from player import Player
from flag import Flag
from minus import Minus

screen = pygame.display.set_mode((720, 700))
pygame.display.set_caption("Labyrinthe")

bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (1800, 1800))
box = pygame.image.load("black-check-box.png")
box = pygame.transform.scale(box, (50, 50))
blank = pygame.image.load("blank.png")
blank = pygame.transform.scale(blank, (50, 50))

flag = Flag()
affichage = Affichage(screen, box, blank)
player = Player(screen)
minus = Minus()

i = 0
run = True


while run:

    screen.blit(bg, (-250, -350))
    minus.start(screen)
    screen.blit(player.image, player.rect )
    flag.start(screen)

    Affichage(screen, box, blank)

    player.Win()
    


    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()


        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                while not player.rect.y == 100 or not pygame.sprite.spritecollide(player, minus.all_minus, False) :
                    if not player.rect.y <= 100: 
                        if not pygame.sprite.spritecollide(player, minus.all_minus, False):
                               player.move_up()
                               continue
                        else:
                            player.move_down()
                            break
                    else:
                        player.move_down()
                        break


            elif event.key == pygame.K_DOWN:
                while not player.rect.y == 600 or not pygame.sprite.spritecollide(player, minus.all_minus, False) :
                    if not player.rect.y >= 600:
                        if not pygame.sprite.spritecollide(player, minus.all_minus, False):
                               player.move_down()
                               continue
                        else:
                            player.move_up()
                            break
                    else:
                        player.move_up()
                        break
                        


            elif event.key == pygame.K_RIGHT:
                while not player.rect.x == 600 or not pygame.sprite.spritecollide(player, minus.all_minus, False) :
                    if not player.rect.x >= 600:
                        if not pygame.sprite.spritecollide(player, minus.all_minus, False):
                               player.move_right()
                               continue
                        else:
                            player.move_left()
                            break
                    else:
                        player.move_left()
                        break


            elif event.key == pygame.K_LEFT:
                print("left")
                while not player.rect.x == 50 or not pygame.sprite.spritecollide(player, minus.all_minus, False) :
                    if not player.rect.x <= 50:
                        if not pygame.sprite.spritecollide(player, minus.all_minus, False):
                               player.move_left()
                               continue
                        else:
                            player.move_right()
                            break
                    else:
                        player.move_right()
                        break
                    



 