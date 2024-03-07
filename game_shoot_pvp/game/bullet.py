from pygame.rect import Rect as Rect
from init import *

class Bullet:
    """
    variable:
    impact_force
    damage
    func:
    is_pouding
    update
    """
    def __init__(self,dir,pos,num) -> None:
        self.num = num
        self.dir = dir
        self.pos = pos
        self.impact_force: int
        self.damage: int

    def is_pounding(self, rect: pygame.Rect):
        pass
    def pound(self)->tuple[int,int]:
        pass
    def disposal(self):
        bullets.remove(self)

    def update(self):
        pass


bullet_img = pic(r"game_shoot_pvp/pic/bullet.png")

class Bullet_common(Bullet):
    def __init__(self, dir, pos, num) -> None:
        super().__init__(dir, pos, num)
        self.img = bullet_img
        self.rect =self.img.get_rect()
        self.rect.center = pos
        self.rect.centery +=10
        self.impact_force = 10
        self.damage =5
        self.speed = BULLET_SPEED
        self.v = self.speed * dir
    def is_out(self):
        return self.rect.centerx<=0 or self.rect.centerx>=SCREEN_LENGTH

    def move(self):
        self.rect.x+=self.v
        self.pos = self.rect.center
        background.blit(self.img,self.rect.topleft)

    def is_pounding(self, rect : pygame.Rect):
        left , right = rect.left,rect.right
        top , bottom = rect.top,rect.bottom
        x , y = self.rect.center
        x_e = self.v + x 
        if ((x_e >=right and x <left) or (x_e >=left and x<right)) and top <= y <= bottom:
            return True

        if left <= x <= right and top <= y <= bottom:
            return True
        return False
    def pound(self) -> tuple[int, int]:
        return (self.dir*self.impact_force,0)
    def update(self):
        self.move()
        if self.is_out():
            self.disposal()
        draw(self.img,self.rect.topleft)

class Bullet_sniper(Bullet_common):
    def __init__(self, dir, pos, num) -> None:
        super().__init__(dir, pos, num)
        self.impact_force = 20
        self.damage = 50
        self.v *= 2



class Stove_ball(Bullet):
    def __init__(self, dir, pos, num) -> None:
        super().__init__(dir, pos, num)
        self.impact_force = 10
        self.idx = 0
        self.damage = 10
        self.stove_lines_posx = [(pos[0]+dir*25+40 * x * dir) for x in range(1,4)]
        self.posy = self.pos[1] + 20
        self.line_length = 50
        self.up_force = 10
    def is_pounding(self, rect: pygame.Rect):
        left, right = rect.left, rect.right
        bottom, top = rect.bottom, rect.top
        if not (top <= self.posy <= bottom):
            return False
        for posx in self.stove_lines_posx:
            if left <= posx <= right:
                return True

    def pound(self) -> tuple[int, int]:
        return (self.dir*self.impact_force , -self.up_force)
    def draw(self):
        posy = self.posy
        for posx in self.stove_lines_posx:
            start_pos = (posx,posy)
            end_pos = (posx,posy-self.line_length)
            pygame.draw.line(screen,green,start_pos,end_pos,5)
    def move(self):
        self.posy -= 10
    def update(self):
        self.draw()
        self.move()
        self.idx += 1
        if self.idx == 18 :
            self.disposal()
        



pi = 3.1415926
rc_v = [(math.cos(pi/18 * i ),math.sin(pi/18 * i )) for i in range(-4,4)]
rotato_pos_l = [(-int(70*x),int(70*y)) for x,y in rc_v]
rotato_pos_r = [(-x,y) for x,y in rotato_pos_l]
rotato_pos = {1:rotato_pos_r,-1:rotato_pos_l}

rotato_v_l  = [(int(math.tan(pi/18*i)*1000+0.5)) for i in range(-4,4)]
rotato_v_r = [(int(math.tan(pi/18*i)*1000+0.5)) for i in range(3,-5,-1)]
rotato_v = {1:rotato_v_r, -1:rotato_v_l}

class BUllet_sword_trace(Bullet):
    def __init__(self, dir, pos, num) -> None:
        super().__init__(dir, pos, num)
        self.impact_force = 20
        self.damage =20

        self.idx = -1
        self.role_x = pos[0]
        self.role_center = pos
    def pound(self) -> tuple[int, int]:
        return (self.dir*self.impact_force,0)
    def is_pounding(self, rect:pygame.Rect):
        rear_pos_x = rotato_pos[self.dir][self.idx][0] + self.role_x
        rear_slope = rotato_v[self.dir][self.idx]    
        if rect.left <= self.role_x <= rect.right:
            return True
        if self.dir == 1:
            if self.role_x > rect.right :
                return False
            p1, p2 = rect.topleft, rect.bottomleft
            k1 = slope_calculate(self.role_center ,p1)
            k2 = slope_calculate(self.role_center ,p2)
            if rear_pos_x >= rect.left and k1 <= rear_slope <= k2:
                return True
        else:
            if self.role_x < rect.left :
                return False
            p1, p2 = rect.bottomright, rect.topright
            k1 = slope_calculate(self.role_center , p1)
            k2 = slope_calculate(self.role_center , p2)
            if rear_pos_x <= rect.right and k1 <= rear_slope <= k2:
                return True
        return False 
    def update(self):
        self.idx += 1
        if self.idx == 8 :
            self.disposal()
            return