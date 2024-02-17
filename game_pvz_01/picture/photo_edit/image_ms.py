import pygame
from pygame.locals import *
import sys
from PIL import Image
path="picture/pic/S.png"
img=Image.open(path)
pygame.init()
# img=img.rotate(180)
img.save(path)
# 设置屏幕大小和标题  
screen_width = 1000  
screen_height = 600  
img_2=pygame.image.load(path)
screen = pygame.display.set_mode((screen_width, screen_height))  
pygame.display.set_caption("图片测量")
a=1
def image_input(file=None,size=100,text=(),color=(0,0,0),pos=(0,0)):    
    p=pygame.font.Font(file, size).render(text, True, color)
    # screen.blit(p,pos)
    return p
def ima_mes(p=pygame.font.Font(None, 100).render("", True, (0,0,0))):
    global pc
    pos=p.get_rect()
    pc=pos.topleft=(200,300)
    l=pos.left
    r=pos.right
    d=pos.bottom
    w=pos.top
    return [l,r,d,w]
# [216, 384, 250, 150]
p=image_input("write_source/black hold.TTF",100,"111")
l=ima_mes(p)
print(l)
# pygame.mouse.get_cursor
while True:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit()  
            sys.exit()
        if event.type == MOUSEBUTTONDOWN :
            mouse_x, mouse_y = pygame.mouse.get_pos()  
            if mouse_x > l[0] and mouse_x < l[1] and mouse_y > l[3] and mouse_y < l[2]: 
                print(21212)
        if event.type==MOUSEWHEEL:
                print(6)
    Press=pygame.key.get_pressed()
    if Press[K_ESCAPE]:
            break
    screen.fill((255,255,255))
    # img=img.rotate(10)
    # a=1
    if a:
        a=0
        size=(100,100)
    else:
        a=1
        size=(60,60)
    img=img.resize(size)
    img.save(path)
    screen.blit(p,pc)
    img_2=pygame.image.load(path)
    screen.blit(img_2,(0,0))
    pygame.display.flip() 
    pygame.time.Clock().tick(20)