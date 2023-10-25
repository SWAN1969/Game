import pygame
pygame.init()

platos = 800
ypsos = 600


pygame.display.set_caption("My_game")

win = pygame.display.set_mode((platos,ypsos))

background = pygame.image.load("pictures/background.png")

playerImg = pygame.image.load('pictures/player.png')


xi=200
yi=300


def player(xi,yi):
    win.blit(playerImg, (xi,yi))




run = True


while run:

    pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    win.blit(background, (0, 0))


    xi+=0.2
    yi-=0.05

    player(xi,yi)


    pygame.display.update() 

  
pygame.quit()           