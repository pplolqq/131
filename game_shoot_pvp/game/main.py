from Role import *
from init import *

class Cloud():
    def __init__(self,rect_val) -> None:
        self.box_rect = pygame.Rect(rect_val)
        self.box_rect.center = self.box_rect.topleft
        self.col_start = (self.box_rect.left,self.box_rect.centery)
        self.col_end = (self.box_rect.right,self.box_rect.centery)
        self.rect = pygame.draw.line(screen,red,self.col_start,self.col_end)
        ground_poses.append(self.box_rect)
        # ground_poses.append(self.rect)
    def update(self):
        pass
def Role_img(color):
    return pic(r"game_shoot_pvp\pic\role_{}.png".format(color))

Kr_player1 = Kr(K_w,K_a,K_d,K_s,K_j)
Kr_player2 = Kr(K_UP,K_LEFT,K_RIGHT,K_DOWN,K_KP_1)

role_1 = Role(Role_img("green"),Kr_player1,0)
role_2 = Role(Role_img("orange"),Kr_player2,1)

role_group = [role_1,role_2]

text_show = pygame.font.Font(None,50)

def text(body,v,color =little_blue):
    return text_show.render(str(body)+str(v),1,color)
def text_draw(role = role_1):
    draw(text("role1_pos: ",role.rect.center),(0,0))
    draw(text("role1_v: ",role.vx),(0,40))
    draw(text("role1_force: ",role.force_x),(0,80))

def draw_line(startpos,endpos,wide=5,color=green):
    pygame.draw.line(screen,color,startpos,endpos,wide)

def cloud_edit(cloud_length):
    mouse_pos = pygame.mouse.get_pos()
    mouse_status = pygame.mouse.get_pressed()
    if mouse_status[0] :
        c =Cloud((mouse_pos,(cloud_length,10)))
        boxes.append(c)
    if mouse_status[2]:
        if boxes:
            boxes.pop()
            ground_poses.pop()
boxes = []

center = (SCREEN_LENGTH//2,SCREEN_WIDTH//2)
back_center = (BACK_LENGTH//2,BACK_WIDTH//2)
commot_center =point_minus(center,back_center)

def mid(p1,p2,key):
    p1 = key(p1)
    p2 = key(p2)
    p = ((p1[0]+p2[0])//2,(p1[1]+p2[1])//2)
    return p
def main():
    running =True
    mouse_pos = pygame.mouse.get_pos()
    cloud_length = 200
    map1_pos = (150,150 )
    rect = background.get_rect()
    rect.center = center
    for pos in ground_poses1:
        x1,x2,y = pos
        ground_poses.append(pygame.draw.line(screen,red,(x1,y),(x2,y),5))
    while running:
        mouse_pos = pygame.mouse.get_pos()
        press=pygame.key.get_pressed()
        if press[K_ESCAPE]:
            running = False
        draw(background,rect.topleft)
        draw(map1,map1_pos)

        for ground in ground_poses:
            ground:pygame.Rect
            # ground.center = point_add(ground.center,pos_differ)
            pygame.draw.rect(screen,red,ground)
        for role in role_group:
            role:Role
            # role.rect.center = point_add(role.rect.center,pos_differ)
            role.update()
        for bullet in bullets:
            bullet:Bullet
            bullet.update()
        t = pygame.event.get(MOUSEBUTTONDOWN)
        if t:
            t= t[0]
            if t.button == 4:
                cloud_length +=10
            if t.button == 5:
                cloud_length -=10
        cloud_edit(cloud_length)
        x,y = mouse_pos
        pygame.draw.line(screen,black,(x+cloud_length//2,y),(x-cloud_length//2,y),5)
        pygame.display.update()
        pygame.time.Clock().tick(60)
if __name__ == "__main__":
    main()
    # for pos in ground_poses:
    #     pos:pygame.Rect
    #     print((pos.left,pos.width,pos.bottom))


class Box:
    def __init__(self) -> None:
        pass
class Role_AI(Role):
    def __init__(self, img, kr: Kr, num) -> None:
        super().__init__(img, kr, num)
        self.status = 0
        self.status_func = []
        self.chased_role : Role = role_1
        self.chased_rect = self.chased_role.rect
        self.chase_pos = self.chased_rect.center
    def update(self):
        self.chased_rect = self.chased_role.rect
        self.chase_pos = self.chased_rect.center
        self.shoot_point = self.chase_pos[1] -10
        self.weapon.update()
    def move(self):
        pass
    def wait(self):
        pass
    def chase(self):
        if self.shoot_point == self.rect.y:
            self.weapon.is_press = True
            pass

        pass
    def check_shoot(self):
        pass
    def attack(self):
        pass