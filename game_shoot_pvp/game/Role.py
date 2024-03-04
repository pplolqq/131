from init import *
from weapon import Weapon,weapon_select
from bullet import Bullet
from blood_slot import Blood_slot

#键盘映射 keyboard_reflection
class Kr:
    def __init__(self,jump,left,right,down,shoot) -> None:
        pass
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
        self.rect.center = (random.randint(200,800),0)
        
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


        self.time = 0
        self.shoot_time=0
    

        self.is_died = False
        self.die_time = 0

        self.text_show = pygame.font.Font(None,50)
        self.text_content = ""
        self.text = self.text_show.render(self.text_content,1,green)
    

            
    def move(self):

        press=pygame.key.get_pressed()
        
        if press[self.kr.left]:
            self.dir=-1
            self.rect.x+=self.dir*self.xmove
        
        if press[self.kr.right]:
            self.dir=1
            self.rect.x+=self.dir*self.xmove
        if press[self.kr.jump] and self.jump_times and not self.press_key_k:
                self.press_key_k =True
                self.jump_times -= 1
                self.is_stand=False
                self.v = -self.jump_speed
        if not press[self.kr.jump] and self.press_key_k:
                self.press_key_k=False
        if press[self.kr.dowm]:
            self.is_stand=False
            self.rect.y+=1

    
    def stand_judge(self):
        for ground in ground_poses:
            if ground[0] <=self.rect.centerx <=ground[1] and self.v>=0 and  self.rect.bottom<=ground[2] and self.rect.bottom+self.v+self.g>=ground[2]:
                self.rect.bottom=ground[2] 
                self.jump_times=self.jump_times_total
                self.g=0
                self.v=0
                return
        self.g=self.gravity
    
    def status_renew(self):
        self.rect.center = (random.randint(200,800),-100)   #随机的重生位置
        self.v,self.vx = 0, 0

    def check_died(self):
        if (self.rect.top>=SCREEN_WIDTH  or self.blood_slot.length <=0) and not self.is_died:
            self.die_time = pygame.time.get_ticks()
            self.is_died = True
            self.rect.y=1000
        if self.is_died:
            self.die()
            
    def die(self):
        self.blood_slot.length = 0
        if self.time - self.die_time >= 1000:
            self.blood_slot.text_update()
            self.status_renew()
            self.is_died =False


    #待重写，抽象到weapon类中
        
    def shoot(self):
        # self.weapon.shoot_check(press[self.kr.shoot])
        if self.press[self.kr.shoot] and self.time - self.shoot_time >= 180:
            self.vx -= self.weapon.back_force * self.dir
            self.shoot_time = pygame.time.get_ticks()
            self.weapon.attack()

    def check_repelled(self):
        for bullet in bullets:
            bullet : Bullet
            if self.num == bullet.num:
                continue
            # if bullet.is_pounding(self.rect) and self.vx == 0:
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

        self.stand_judge()
        self.move()
        # self.shoot()
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
        self.weapon.is_shoot = self.press[self.kr.shoot]
        self.weapon.update()