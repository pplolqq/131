from init import *
from bullet import *

class Weapon:
    """
attrs_of_weapon:
    attack_v
    back_force
    repel_force
    bullet_num
    shoot_style
"""
    def __init__(self):
        # self.weapon_im
        # self.weapon_img_r = pic(r"game_shoot_pvp\pic\gun_l.png"),pic(r"game_shoot_pvp\pic\gun.png")

        self.back_force: int
        #common_args
        self.idx = 0
        self.dir : int = 1 
        self.pos : list[int, int]
        self.time : int
        self.num : int

    def attack(self):
        pass
    def update(self):
        pass

class Common_Gun(Weapon):
    def __init__(self):
        super().__init__() 
        self.img_list = {1:pic(r"game_shoot_pvp\pic\gun_R.png"),-1:pic(r"game_shoot_pvp\pic\gun_L.png")}
        self.back_force = 5
    def attack(self):
        bullets.append(Bullet_common(self.dir,self.pos,self.num))

    def update(self):
        self.img = self.img_list[self.dir]
        if self.dir == 1 :
            draw(self.img,self.pos)
        else:
            draw(self.img,point_minus(self.pos,(40,0)))

pic_staves_l = [pic(fr"game_shoot_pvp\z_temp\L\{i}.png") for i in range(1,9)]
pic_staves_r = [pic(fr"game_shoot_pvp\z_temp\R\{i}.png") for i in range(1,9)]    
pic_staves = {1:pic_staves_r,-1:pic_staves_l}

class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self.img:pygame.Surface = pic(r"game_shoot_pvp\z_temp\L\1.png")
        self.rect = self.img.get_rect()
        self.back_force = 0
        self.is_attack = False
    def attack(self):
        self.is_attack = True
        self.time = get_time()
    def slash(self):
        if get_time() - self.time >= 2:
            self.idx += 1
            if self.idx == 1:
                bullets.append(BUllet_sword_trace(self.dir,self.pos,self.num))
            if self.idx == 8:
                self.idx = 0
                self.is_attack = False
            self.time = get_time()
        # stave_rear_pos = point_add(self.rect.center,rotato_pos[self.dir][self.idx])
        # pygame.draw.line(screen,green,self.rect.center,stave_rear_pos,5)

    def update(self):
        self.img = pic_staves[self.dir][self.idx]
        self.rect.center = point_add(self.pos,(0,10))
        if self.is_attack:
            self.slash()
        draw(self.img,self.rect.topleft)
    def generate(self):
        return Sword()

weapon_select = [Sword(),Common_Gun()]
