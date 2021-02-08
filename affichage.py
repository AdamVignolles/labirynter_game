import pygame



class Affichage():
    def __init__(self, screen, box, blank):
        super().__init__()
        self.i = 50
        screen.blit(box, (50,100))
        screen.blit(box, (100,100))
        screen.blit(box, (150,100))
        screen.blit(box, (200,100))
        screen.blit(box, (250,100))
        screen.blit(box, (300,100))
        screen.blit(box, (350,100))
        screen.blit(box, (400,100))
        screen.blit(box, (450,100)) 
        screen.blit(box, (500,100))
        screen.blit(box, (550,100))
        screen.blit(box, (600,100))

        screen.blit(box, (50,600))
        screen.blit(box, (100,600))
        screen.blit(box, (150,600))
        screen.blit(box, (200,600))
        screen.blit(box, (250,600))
        screen.blit(box, (300,600))
        screen.blit(box, (350,600))
        screen.blit(box, (400,600))
        screen.blit(box, (450,600)) 
        screen.blit(box, (500,600))
        screen.blit(box, (550,600))
        screen.blit(box, (600,600))

        screen.blit(box, (50,100))
        screen.blit(box, (50,150))
        screen.blit(box, (50,200))
        screen.blit(box, (50,250))
        screen.blit(box, (50,300))
        screen.blit(box, (50,350))
        screen.blit(box, (50,400))
        screen.blit(box, (50,450))
        screen.blit(box, (50,500)) 
        screen.blit(box, (50,550))
        screen.blit(box, (50,600))

        screen.blit(box, (600,100))
        screen.blit(box, (600,150))
        screen.blit(box, (600,200))
        screen.blit(box, (600,250))
        screen.blit(box, (600,300))
        screen.blit(box, (600,350))
        screen.blit(box, (600,400))
        screen.blit(box, (600,450))
        screen.blit(box, (600,500)) 
        screen.blit(box, (600,550))
        screen.blit(box, (600,600))

        while self.i < 600:
            self.i+=50
            screen.blit(blank, (self.i,150))
            screen.blit(blank, (self.i,200))
            screen.blit(blank, (self.i,250))
            screen.blit(blank, (self.i,300))
            screen.blit(blank, (self.i,350))
            screen.blit(blank, (self.i,400))
            screen.blit(blank, (self.i,450))
            screen.blit(blank, (self.i,500))
            screen.blit(blank, (self.i,550))
    
    
        
