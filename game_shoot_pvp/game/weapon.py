from bullet import Bullet
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
        self.is_shoot = False
        self.is_press = False #role's shoot key
        self.shoot_time = 0
        self.shoot_interval = 180
        #common_args
        self.idx = 0   #类内计时
        self.back_force: int
        self.dir : int = 1 
        self.pos : tuple[int, int]
        self.time : int
        self.num : int
    def shoot(self,Bullet_type:Bullet):
        bullets.append(Bullet_type(self.dir,self.pos,self.num))


    def press_judge(self):
        if self.is_press and self.time - self.shoot_time >= self.shoot_interval:
            self.shoot_time = self.time
            return True
        return False
    
    def shoot_check(self):
        pass
    def update(self):
        pass
#region commongun
class Common_Gun(Weapon):
    def __init__(self):
        super().__init__() 
        self.img_list = {1:pic(r"game_shoot_pvp\pic\gun_R.png"),-1:pic(r"game_shoot_pvp\pic\gun_L.png")}
        self.back_force = 2
        self.rect = self.img_list[self.dir].get_rect()
        self.shoot_interval = 240
    def shoot_check(self):
        if self.press_judge():
            self.is_shoot = True
            self.shoot(Bullet_common)
    def update(self):
        self.shoot_check()
        self.img = self.img_list[self.dir]
        self.rect.center = self.pos
        draw_pos = point_add(self.rect.topleft,(0,10))
        draw(self.img,draw_pos)
#endregion


#region sword
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
        self.shoot_time = 0
        self.shoot_interval = 500
    def shoot_check(self):
        if self.press_judge():
            self.is_attack = True

        if self.is_attack :
            self.slash()

    def slash(self):
        self.idx += 1
        if self.idx == 8:
            self.idx = 0
            self.is_shoot = True
            self.is_attack = False
            self.shoot(Stove_ball)
    def update(self):
        self.shoot_check()
        self.img = pic_staves[self.dir][self.idx]
        self.rect.center = point_add(self.pos,(0,10))
        draw(self.img,self.rect.topleft)

#endregion
class Charge_Gun(Common_Gun):
    def __init__(self):
        super().__init__()
        self.charge_total_length = 40
        self.charge_x = 0
        self.is_charge = False
        self.is_full = False
        self.back_force = 5

    def shoot_check(self):
        if self.is_press:
            self.is_charge = True
        else:
            self.idx = 0
        if self.is_charge :
            self.charge()

    def charge(self):
        x = self.pos[0] - self.dir * (self.charge_total_length//2)
        y = self.pos[1] - ROLE_LENGTH//2
        if self.idx:
            pygame.draw.line(screen,red,(x,y),(x+self.dir*self.idx,y),5)
        if self.idx >= self.charge_total_length:
            self.idx = self.charge_total_length
            x = self.pos[0] + self.dir * (ROLE_WIDTH//2)
            y = self.pos[1]
            pygame.draw.line(screen,white,(x,y),(x+self.dir*1000,y),2)
            self.is_full = True
        self.idx += 2
    
        if self.is_full and not self.is_press:
            self.is_shoot = True
            self.is_charge = False
            self.is_full = False
            self.idx = 0
            self.shoot(Bullet_sniper)
            
weapons = [Sword,Charge_Gun,Common_Gun]

weapon_select_id = [1,2]


weapon_select = []
for id in weapon_select_id:
    weapon = weapons[id]
    weapon_select.append(weapon())
