from Init import *
import random
botton_pic=[pic(fr"game_pvz_01\picture\pic_temp\No{i}.png")  for i in range(22)]
class botton:
    def __init__(self,region:pygame.Rect) -> None:
        self.pos = 1
        self.region= region
    def on_click(self):
        if self.region.left<=get_mouse_pos()[0]<=self.region.right\
        and self.region.top<=get_mouse_pos()[1]<=self.region.bottom:
            return True
        return False
class sun:
    def __init__(self):
        self.frame_idx=0
        self.pic:pygame.image=botton_pic[self.frame_idx]
        self.pos=(random.randint(100,900),0)
        self.rect=self.pic.get_rect()
        self.botton=botton(self.rect)
    def on_click(self):
        if self.botton.on_click():
            print(1)
    def generate(self):
        
        pass
    def update(self):
        if self.rect.y<500:
            self.rect.y+=10
        else:
            pass

    pass
