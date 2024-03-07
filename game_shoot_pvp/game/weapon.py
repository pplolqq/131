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
        self.bullet_type: Bullet
        self.draw_pos:tuple[int, int]
        self.img: pygame.Surface
    def shoot(self,):
        bullets.append(self.bullet_type(self.dir,self.pos,self.num))


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
        self.bullet_type = Bullet_common
        self.draw_pos = (ROLE_LENGTH//2,ROLE_WIDTH//2)
    def shoot_check(self):
        if self.press_judge():
            self.is_shoot = True
            self.shoot()
    def update(self):
        self.shoot_check()
        self.img = self.img_list[self.dir]
        self.rect.center = point_add(self.pos,(0,10))
        self.draw_pos = self.rect.topleft
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
        self.bullet_type = Stove_ball
        self.draw_pos = (ROLE_LENGTH//2,ROLE_WIDTH//2)
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
            self.shoot()
    def update(self):
        self.shoot_check()
        self.img = pic_staves[self.dir][self.idx]
        self.rect.center = point_add(self.pos,(0,10))
        self.draw_pos = self.rect.topleft
#endregion
class Charge_Gun(Common_Gun):
    def __init__(self):
        super().__init__()
        self.charge_total_length = 40
        self.is_full = False
        self.back_force = 10
        self.bullet_type = Bullet_sniper
        self.status_func = [self.shoot_status0,self.shoot_status1]
        self.status = 0
    def trans_status(self,status):
        self.status = status
        self.status_func[self.status]()
    def shoot_status0(self):
        if self.is_press:
            self.idx += 2
        else:
            self.idx =0
        if self.idx >= self.charge_total_length:
            self.trans_status(1)
    def shoot_status1(self):
        if not self.is_press:
            self.shoot()
            self.is_shoot = True
            self.trans_status(0)
        self.idx = self.charge_total_length
        x = self.pos[0] + self.dir * (ROLE_WIDTH//2)
        y = self.pos[1]
        pygame.draw.line(screen,white,(x,y),(x+self.dir*1000,y),2)
    def shoot_check(self):
        self.trans_status(self.status)
        x = self.pos[0] - self.dir * (self.charge_total_length//2)
        y = self.pos[1] - ROLE_LENGTH//2
        if self.idx:
            pygame.draw.line(screen,red,(x,y),(x+self.dir*self.idx,y),5)
    # def shoot_check(self):
    #     if self.is_press:
    #         self.charge()
    #     else:
    #         self.idx = 0
    #     if self.is_full and not self.is_press:
    #             self.is_shoot = True
    #             self.is_full = False
    #             self.shoot()
    def charge(self):
        x = self.pos[0] - self.dir * (self.charge_total_length//2)
        y = self.pos[1] - ROLE_LENGTH//2
        if self.idx:
            pygame.draw.line(screen,red,(x,y),(x+self.dir*self.idx,y),5)
        if self.idx >= self.charge_total_length:
            self.is_full = True
            self.idx = self.charge_total_length
            x = self.pos[0] + self.dir * (ROLE_WIDTH//2)
            y = self.pos[1]
            pygame.draw.line(screen,white,(x,y),(x+self.dir*1000,y),2)
        self.idx += 2
    
       
            
weapons = [Sword,Charge_Gun,Common_Gun]

weapon_select_id = [1,2]


weapon_select = []
for id in weapon_select_id:
    weapon = weapons[id]
    weapon_select.append(weapon())
