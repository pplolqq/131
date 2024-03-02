from init import *

bullet_img = pic(r"game_shoot_pvp/pic/bullet.png")
class Bullet:
    def __init__(self,dir,pos,num) -> None:
        self.num = num
        self.img = bullet_img
        self.rect =self.img.get_rect()

        self.rect.center = pos
        self.rect.centery +=10
        if dir == -1:
            self.rect.x-=10  #调整位置
        self.dir = dir
        self.pos = pos

        self.impact_force: int
        self.damage: int

    def is_pounding(self, rect: pygame.Rect, num):
        pass
    def is_out(self):
        return self.rect.centerx<=0 or self.rect.centerx>=SCREEN_LENGTH
    def disposal(self):
        bullets.remove(self)

    def move(self):
        pass
    def update(self):
        self.move()
        if self.is_out():
            self.disposal()

class Bullet_common(Bullet):
    def __init__(self, dir, pos, num) -> None:
        super().__init__(dir, pos, num)
        self.impact_force = 10
        self.damage =5
        self.speed = BULLET_SPEED
        self.v = self.speed * dir

    def move(self):
        self.rect.x+=self.v
        self.pos = self.rect.center
        draw(self.img,self.rect.topleft)

    def is_pounding(self, rect : pygame.Rect, num):
        if self.num == num :
            return False
        left , right = rect.left,rect.right
        top , bottom = rect.top,rect.bottom
        x , y = self.rect.center
        if left <= x <= right and top <= y <= bottom:
            return True
        return False
    

class BUllet_sword_trace(Bullet):
    def __init__(self, dir, pos, num) -> None:
        super().__init__(dir, pos, num)
        self.move_start_time = get_time()
        self.idx = 0
        self.impact_force = 10
        self.damage =20
        
    def move(self):
        self.idx += 1
        if self.idx == 8 :
            self.disposal()
            return
        self.pos = point_add(self.rect.center,rotato_pos[self.dir][self.idx])

    def is_pounding(self, rect, num):
        if self.num == num:
            return False
        rear_pos_x = self.pos[0]
        role_center = self.rect.center
        role_x = self.rect.centerx
        rear_slope = rotato_v[self.dir][self.idx]
        if rect.left <= role_x <= rect.right:
            return True
        if self.dir == 1:
            if role_x > rect.right :
                return False
            p1, p2 = rect.topleft, rect.bottomleft
            k1 = slope_calculate(role_center ,p1)
            k2 = slope_calculate(role_center ,p2)
            if rear_pos_x >= rect.left and k1 <= rear_slope <= k2:
                return True
        else:
            if role_x < rect.left :
                return False
            p1, p2 = rect.bottomright, rect.topright
            k1 = slope_calculate(role_center , p1)
            k2 = slope_calculate(role_center , p2)
            if rear_pos_x <= rect.right and k1 <= rear_slope <= k2:
                return True
        return False 