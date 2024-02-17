import pygame.examples.stars

from Init import *

class Plant:
    def __init__(self, id, pos_dot):
        self.id=id
        self.row,self.column=pos_dot
        self.img_num=0
        self.img_set=pic_set[id].gif
        self.plant_img=pic(self.img_set[self.img_num])
        self.rect:pygame.Rect = self.plant_img.get_rect()
        self.rect.center= grass_pos[self.row][self.column]
        self.put_time=get_time()
        self.is_change=False

    def gif(self):
        self.time=get_time()
        if self.time-self.put_time>=50:
            self.put_time=self.time
            self.img_num+=1
            self.img_num%=info_set[self.id][1]
            self.plant_img=pic(self.img_set[self.img_num])
    def death(self):
        if pygame.mouse.get_pressed()[1]:
            pass


    def update(self):
        self.gif()
        draw(self.plant_img, self.rect.topleft)
