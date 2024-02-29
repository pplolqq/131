import pygame
from pygame.locals import *

import random

pygame.init()
SCREEN_LENGTH = 1000
SCREEN_WIDTH = 600
screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))
pygame.display.set_caption("shoot_pvp")

pic = pygame.image.load
draw = screen.blit

background = pic(r"game_shoot_pvp\pic\back1.png")
map1 = pic(r"game_shoot_pvp\pic\map1.png")


ground_poses=[[165, 345, 200], [440, 580, 180], [680, 850, 175], [265, 740, 250], [165, 326, 350], [370, 600, 350], [680, 870, 330],[780,885,235]]
#键盘映射 keyboard_reflection
class Kr:
    def __init__(self,jump,left,right,down,shoot) -> None:
        pass
        self.jump = jump
        self.left = left
        self.right = right
        self.dowm = down
        self.shoot = shoot



class Weapon:
    """
attrs_of_weapon:
    attack_v
    back_force
    repel_force
    bullet_num
    shoot_style
"""
    def __init__(self,weapon_img_l,weapon_img_r):
        self.weapon_img_l = weapon_img_l
        self.weapon_img_r = weapon_img_r
    def shoot(self,dir,pos,num):
        bullets.append(Bullet(dir,pos,num))
    def update(self,dir,pos):
        if dir == 1:
            draw(self.weapon_img_r,pos)
        else:
            draw(self.weapon_img_l,point_minus(pos,(40,0)))


#  实现role类和weapon 类的组合
bullets = []
bullet_img = pic(r"game_shoot_pvp/pic/bullet.png")
class Bullet:
    def __init__(self,dir,pos,num,attrs = None) -> None:

        self.num = num

        self.v = 30*dir
   
        self.img = bullet_img

        self.rect =self.img.get_rect()
    
        self.rect.center = pos

        self.rect.centery +=10

        if dir == -1:
            self.rect.x-=10  #调整位置

        self.dir = dir
    def is_beat(self):
        for role in role_group:
            if role.rect.left<=self.rect.centerx<=role.rect.right  and role.rect.top<=self.rect.centery <= role.rect.bottom and self.num != role.num:
                role.repelled(self.dir)
                role.is_repelled= True
                return True
        
        return False
    def is_out(self):
        return self.rect.centerx<=0 or self.rect.centerx>=SCREEN_LENGTH
    
    def disposal(self):
        bullets.remove(self)
    def update(self):
        self.rect.x+=self.v
        draw(self.img,self.rect.topleft)
        if self.is_beat() or self.is_out():
            self.disposal()

def point_add(p, q):
    return (p[0] + q[0], p[1] + q[1])
def point_minus(p, q):
    return (p[0] - q[0], p[1] - q[1])
class Blood_slot:
    def __init__(self,color,pos):
        self.text_style = pygame.font.Font(None,50)

        self.pos = pos 
    
        self.border_color = (255,255,255)

        rect_border = 5

        self.pos_rect = self.pos
        self.l_w_rect = (160,50)
        
        self.pos_rect_back = point_add(self.pos_rect,(rect_border,rect_border))
        self.l_w_rect_back = (50,50)

        self.pos_role = point_add(self.pos_rect,(rect_border,rect_border))
        self.l_w_role = point_minus(self.l_w_rect_back,(2*rect_border,2*rect_border))
        self.role_color = color

        self.pos_blood_slot = point_add(self.pos_rect, (-20,50))
        self.l_w_blood_slot = (200,50)

        self.pos_blood_back = point_add(self.pos_blood_slot,(rect_border,rect_border))
        self.l_w_blood_back = point_minus(self.l_w_blood_slot,(2*rect_border,2*rect_border))
        self.blood_back_color = (125,125,125) #灰色

        self.pos_blood = self.pos_blood_back
        self.l_w_blood = self.l_w_blood_back
        
        self.blood_length = 190
        self.length = self.blood_length
        self.blood_color = (0,255,0) #绿色

        self.lives = 15
        self.text = self.text_style.render(str(self.lives),True,(255,255,255))

    def text_update(self):
        self.lives -= 1
        self.length = self.blood_length
        self.text = self.text_style.render(str(self.lives),True,(255,255,255))   
    def draw(self):
        self.l_w_blood = (self.length,40)
        pygame.draw.rect(screen,self.border_color,pygame.Rect(self.pos_rect,self.l_w_rect),5)
        pygame.draw.rect(screen,self.border_color,pygame.Rect(self.pos_rect,self.l_w_rect_back),5)
        pygame.draw.rect(screen,self.role_color,pygame.Rect(self.pos_role,self.l_w_role),0)
        pygame.draw.rect(screen,self.blood_back_color,pygame.Rect(self.pos_blood_back,self.l_w_blood_back),0,10)
        pygame.draw.rect(screen,self.blood_color,pygame.Rect(self.pos_blood,self.l_w_blood),0,10)
        pygame.draw.rect(screen,self.border_color,pygame.Rect(self.pos_blood_slot,self.l_w_blood_slot),5,20)
        draw(self.text,(self.pos_role[0]+60,self.pos_role[1]+5))

common_weapon = Weapon(pic(r"game_shoot_pvp\pic\gun_l.png"),pic(r"game_shoot_pvp\pic\gun.png"))
class Role:
    def __init__(self,img,kr:Kr,bs,num) -> None:
        
        self.num = num
        self.kr=kr
        self.role : pygame.Surface = img
        self.blood_slot : Blood_slot = bs

        self.rect = self.role.get_rect()
        self.rect.center = (random.randint(200,800),0)

        self.v = 0
        self.g = 1        #竖直重力


        self.vx = 0
        self.force_x = 0 #水平方向的力 
        
        self.is_stand=False
        self.jump_times_total=3
        self.jump_times=self.jump_times_total
        self.press_key_k=False
        
        
        self.dir = 1     #1 为右 ，-1 为左
        self.xmove= 10      #按一次移动的移动量
        self.press = None

        self.weapon = common_weapon 

        self.time = 0
        self.shoot_time=0
    

        self.is_repelled = False

        self.is_died = False
        self.die_time = 0


    def shoot(self):
        press = pygame.key.get_pressed()
        
        if press[self.kr.shoot] and self.time - self.shoot_time >= 180:
            self.vx -= 10 * self.dir
            self.force_x += self.dir
            self.shoot_time = pygame.time.get_ticks()
            self.weapon.shoot(self.dir,self.rect.center,self.num)

        if self.vx*self.force_x > 0:
            self.vx -= self.force_x * 2
            self.rect.x+=self.vx
        
    def move(self):

        press=pygame.key.get_pressed()
        
        if press[self.kr.left]:
            self.dir=-1
            self.rect.x+=self.dir*self.xmove
        
        if press[self.kr.right]:
            self.dir=1
            self.rect.x+=self.dir*self.xmove
        if press[self.kr.jump] and self.jump_times and not self.press_key_k:
                self.press_key_k=True
                self.jump_times-=1
                self.is_stand=False
                self.v=-12
        if not press[self.kr.jump] and self.press_key_k:
                self.press_key_k=False
        if press[self.kr.dowm]:
            self.is_stand=False
            self.rect.y+=1

        self.v+=self.g
        self.rect.y+=self.v
    
    def stand_judge(self):
        for ground in ground_poses:
            if ground[0] <=self.rect.centerx <=ground[1] and self.v>=0 and  self.rect.bottom<=ground[2] and self.rect.bottom+self.v+self.g>=ground[2]:
                self.rect.bottom=ground[2] 
                self.jump_times=self.jump_times_total
                self.g=0
                self.v=0
                return
        
        self.g=1
    
    #died 重写为状态机函数 ---> 判断 -- 执行
    def died(self):
        if (self.rect.top>=SCREEN_WIDTH  or self.blood_slot.length <=0) and not self.is_died:
            self.die_time = pygame.time.get_ticks()
            self.is_died = True
            self.rect.y=1000


        if self.is_died:
            self.blood_slot.length = 0
        if self.is_died and self.time - self.die_time >= 1000:

            self.blood_slot.text_update()
            self.rect.center = (random.randint(200,800),-100)
            self.v = 0
            self.is_died =False

    def repelled(self,dir):
        self.vx+=dir*20
        self.force_x=dir
        self.blood_slot.length -= 20
    
    #负责人物位置相关常数的更新
    def status_update(self):
        pass
    
    def update(self):
        self.time = pygame.time.get_ticks()

        self.stand_judge()
        self.move()
        self.shoot()
        self.died()

        draw(self.role,self.rect.topleft)


        self.weapon.update(self.dir,self.rect.center)
        self.blood_slot.draw()

def Role_img(color):
    return pic(r"game_shoot_pvp\pic\role_{}.png".format(color))


Kr_player1 = Kr(K_w,K_a,K_d,K_s,K_j)
Kr_player2 = Kr(K_UP,K_LEFT,K_RIGHT,K_DOWN,K_KP_1)

orange = (255,125,40)
green = (180,230,30)

bs1 = Blood_slot(green,(270,400))
bs2 = Blood_slot(orange,(600,400))

role_1 = Role(Role_img("green"),Kr_player1,bs1,1)
role_2 = Role(Role_img("orange"),Kr_player2,bs2,2)
role_group = [role_1,role_2]

color_selected = [green,orange]

text_show = pygame.font.Font(None,50)

little_blue = (0,200,255)


def text(body,v,color =little_blue):
    return text_show.render(str(body)+str(v),1,color)
def text_draw():
    draw(text("role1_v: ",role_1.vx),(0,0))
    draw(text("role1_force: ",role_1.force_x),(0,40))
    draw(text("role2_v: ",role_2.vx),(0,80))
    draw(text("role2_force: ",role_2.force_x),(0,120))

def main():
    running =True
    while running:
        press=pygame.key.get_pressed()
        for even in pygame.event.get():
            if even.type == QUIT:
                running = False
            if even.type == MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        if press[K_ESCAPE]:
            running = False
        draw(background,(0,0))
        draw(map1,(150,150))
        # for ground in ground_poses:
            # pygame.draw.line(screen,(255,0,0),(ground[0],ground[2]),(ground[1],ground[2]),5)

        for role in role_group:
            role:Role
            role.update()
        for bullet in bullets:
            bullet:Bullet
            bullet.update()
        
        text_draw()
        pygame.display.flip()
        pygame.time.Clock().tick(60)
if __name__ == "__main__":
    main()