from init import *
from weapon import Weapon,weapon_select
from bullet import Bullet
from blood_slot import Blood_slot
random_revive_left = 200 
random_revive_right = 800
pos_y = -100 

die_height = 1000 
die_wait_height = SCREEN_WIDTH 
def random_pos():
    return (random.randint(random_revive_left,random_revive_right),pos_y)

#键盘映射 keyboard_reflection
class Kr:
    def __init__(self,jump,left,right,down,shoot) -> None:
        self.jump = jump
        self.left = left
        self.right = right
        self.dowm = down
        self.shoot = shoot

class Role:
    def __init__(self,img,kr:Kr,num) -> None:
        
        self.num = num
        self.kr=kr
        self.role : pygame.Surface = img
        
        self.rect = self.role.get_rect()
        self.rect.center = random_pos()
        
        self.blood_slot : Blood_slot = Blood_slot(color_selected[num],(1000//(2*player_total+1)*(2*num+1),400))
        
        
        self.weapon:Weapon = weapon_select[self.num]
        self.weapon.num = num

        self.v = 0
        self.gravity = GRAVITY
        self.g = self.gravity     #竖直重力
        self.jump_speed = JUMP_SPEED

        self.vx = 0
        self.force_x = 0 #水平方向的力 
        self.friction_constant = 2 #用于水平方向收到速度后的摩擦减速系数
        
        self.is_stand=False
        self.jump_times_total=3
        self.jump_times=self.jump_times_total
        self.press_key_k=False
        
        
        self.dir = 1     #1 为右 ，-1 为左
        self.move_speed = PLAYER_MOVE_SPEED
        self.xmove= self.move_speed      #按一次移动的移动量
        self.press = None
        self.ismove = False


        self.time = 0
        self.shoot_time=0
    

        self.is_died = False
        self.die_time = 0

        self.text_show = pygame.font.Font(None,50)
        self.text_content = ""
        self.text = self.text_show.render(self.text_content,1,green)
    
    def move(self):
        self.rect.x +=self.dir*self.xmove

    def jump(self):
        self.is_stand=False
        self.v = -self.jump_speed



    def check_jump(self):
        if self.press[self.kr.jump] and self.jump_times and not self.press_key_k:
                self.press_key_k =True
                self.jump_times -= 1
                self.jump()
        if not self.press[self.kr.jump] and self.press_key_k:
                self.press_key_k=False

        if self.press[self.kr.dowm]:
            self.is_stand=False
            self.rect.y+=1


    def check_move(self):
        if self.press[self.kr.left]:
            self.dir = -1
            self.ismove = True
        elif self.press[self.kr.right]:
            self.ismove = True
            self.dir = 1
        if self.ismove:
            self.move()
            self.ismove = False
    
    def stand(self):
        self.jump_times=self.jump_times_total
        self.g=0
        self.v=0

    def check_stand(self):
        for ground in ground_poses:
            ground:pygame.Rect
            left,right,bottom = ground.left,ground.right,ground.bottom
            x,y = self.rect.centerx,self.rect.bottom
            if left <= x <= right and self.v >=0 and y<=bottom and y+self.v+self.g >=bottom:
                self.rect.bottom = bottom
            # if ground[0] <=self.rect.centerx <=ground[1] and self.v>=0 and  self.rect.bottom<=ground[2] and self.rect.bottom+self.v+self.g>=ground[2]:
                # self.rect.bottom=ground[2] 
                self.stand()
                return
        self.g=self.gravity
    
    def status_renew(self):
        self.rect.center = random_pos()  #随机的重生位置
        self.v,self.vx = 0, 0

    def check_died(self):
        if (self.rect.top>= die_height  or self.blood_slot.length <=0) and not self.is_died:
            self.die_time = pygame.time.get_ticks()
            self.is_died = True
            self.rect.y= die_wait_height
        if self.is_died:
            self.die()
            
    def die(self):
        self.blood_slot.length = 0
        if self.time - self.die_time >= 1000:
            self.blood_slot.text_update()
            self.status_renew()
            self.is_died =False


    def shoot_back_impulse(self):
        self.vx -= self.dir *self.weapon.back_force
        
    def check_shoot(self):
        if self.weapon.is_shoot:
            self.shoot_back_impulse()
            self.weapon.is_shoot = False

    def check_repelled(self):
        for bullet in bullets:
            bullet : Bullet
            if self.num == bullet.num:
                continue
            if bullet.is_pounding(self.rect) :
                self.repelled(bullet.pound(),bullet.damage)
                bullet.disposal()
                # print("play_"+str(self.num)+"受到了"+str())
 
    def repelled(self,bullet_force:tuple[int,int],damage):
        self.vx,self.v = point_add((self.vx,self.v),bullet_force)
        self.blood_slot.length -= damage
    
    #负责人物位置相关常数的更新
    def status_update(self):
        self.v+=self.g
        self.rect.y+=self.v

        if self.vx != 0 :
            self.force_x = 1 if self.vx < 0 else -1
            if self.vx*self.force_x < 0:
                self.vx += self.force_x 
        else:
            self.force_x = 0
        self.rect.x += self.vx
            
    def update(self):
        self.time = pygame.time.get_ticks()
        self.press = pygame.key.get_pressed()
        self.check_stand()
        self.check_move()
        self.check_jump()
        self.check_shoot()
        self.check_repelled()
        self.check_died()
        self.status_update()
        draw(self.role,self.rect.topleft)
        self.weapon_update()  
        self.blood_slot.update()

    def weapon_update(self):
        self.weapon.dir = self.dir
        self.weapon.pos = self.rect.center
        self.weapon.time = self.time
        self.weapon.is_press = self.press[self.kr.shoot]
        self.weapon.update()
        draw(self.weapon.img,self.weapon.draw_pos)