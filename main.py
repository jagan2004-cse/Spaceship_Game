import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
#ICON
pygame.display.set_caption("ONLINE__SPACE")
icon=pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
#player
playerImg=pygame.image.load('001-spaceship.png')
playerX=370
playerY=480
playerX_change=0
def player(x,y):
    screen.blit(playerImg,(x,y))
running=True
while running:


    screen.fill((128, 128, 128))



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            print("a key is pressed")
            if event.type==pygame.K_LEFT:
                playerX_change=-0.1
                print("left key is pressed")
            if event.type==pygame.K_RIGHT:
                playerX_change=0.1
                print("right key is pressed")
        if event.type==pygame.KEYUP:
            if event.type==pygame.K_LEFT or event.type==pygame.K_RIGHT:
                playerX_change=0.1



    playerX+=playerX_change
    player(playerX,playerY)
    pygame.display.update()


