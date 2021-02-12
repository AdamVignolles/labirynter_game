import pygame
from affichage import Affichage
from player import Player
from flag import Flag
from minus import Minus
import json

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
player = Player()
minus = Minus()

with open('level.json', 'w') as outfile:
    json.dump(1, outfile)


i = 0
run = True




while run:

    screen.blit(bg, (-250, -350))
    minus.start(screen, player)
    screen.blit(player.image, player.rect )
    flag.start(screen)

    Affichage(screen, box, blank)

    player.Win(screen)
    


    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()


        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                while not player.rect.y == 100 or not pygame.sprite.spritecollide(player, minus.all_minus, False):
                    if not player.rect.y <= 100: 
                        if not pygame.sprite.spritecollide(player, minus.all_minus, False):
                            player.move_up(screen)
                            if player.rect.colliderect(flag):
                                player.win = True
                                player.Win(screen)
                                break
                            else:
                                player.win = False
                                continue
                        else:
                            player.move_down(screen)
                            break
                    else:
                        player.move_down(screen)
                        break


            elif event.key == pygame.K_DOWN:
                while not player.rect.y == 600 or not pygame.sprite.spritecollide(player, minus.all_minus, False) :
                    if not player.rect.y >= 600:
                        if not pygame.sprite.spritecollide(player, minus.all_minus, False):
                            player.move_down(screen)
                            if player.rect.colliderect(flag):
                                player.win = True
                                player.Win(screen)
                                break
                            else:
                                player.win = False
                                continue    
                        else:
                            player.move_up(screen)
                            break
                    else:
                        player.move_up(screen)
                        break
                        


            elif event.key == pygame.K_RIGHT:
                while not player.rect.x == 600 or not pygame.sprite.spritecollide(player, minus.all_minus, False):
                    if not player.rect.x >= 600:
                        if not pygame.sprite.spritecollide(player, minus.all_minus, False):
                            player.move_right(screen)
                            if player.rect.colliderect(flag):
                                player.win = True
                                player.Win(screen)
                                break
                            else:
                                player.win = False
                                continue
                        else:
                            player.move_left(screen)
                            break
                    else:
                        player.move_left(screen)
                        break


            elif event.key == pygame.K_LEFT:
                print("left")
                while not player.rect.x == 50 or not pygame.sprite.spritecollide(player, minus.all_minus, False):
                    if not player.rect.x <= 50:
                        if not pygame.sprite.spritecollide(player, minus.all_minus, False):
                            player.move_left(screen)
                            if player.rect.colliderect(flag):
                                player.win = True
                                player.Win(screen)
                                break
                            else:
                                player.win = False
                                continue
                        else:
                            player.move_right(screen)
                            break
                    else:
                        player.move_right(screen)
                        break
                    



 