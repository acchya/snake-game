import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.set_mode((800,600))
pygame.display.set_caption('snake')
white=(255,255,255)
blue=(0,0,225)
red=(255,0,0)
game_over=True
x1=300
y1=300

x1_change=0
y1_change=0

clock=pygame.time.Clock()
while  game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=False
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change=0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change=0
            elif event.key == pygame.K_UP:
                x1_change =0
                y1_change=-10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change=10
    x1 +=x1_change
    y1 +=y1_change
    dis.fill(white)
    pygame.draw.rect(dis,blue,[x1,y1,20,20])
    clock.tick(30)
    pygame.display.update()
pygame.quit()
quit()
