from Role import *
from cloud import *
from weapon import *
from init import *

#role_init
def Role_img(color):
    return pic(r"game_shoot_pvp\pic\role_{}.png".format(color))
Kr_player1 = Kr(K_w,K_a,K_d,K_s,K_j)
Kr_player2 = Kr(K_UP,K_LEFT,K_RIGHT,K_DOWN,K_KP_1)
weapons = [Stove,Charge_Gun,Common_Gun]
weapon_select_id = [0,2]
weapon_select = []
for id in weapon_select_id:
    weapon = weapons[id]
    weapon_select.append(weapon())

role_1 = Role(Role_img("green"),Kr_player1,weapon_select[0],0)
role_2 = Role(Role_img("orange"),Kr_player2,weapon_select[1],1)
role_group = [role_1,role_2]


#cloud_init
for pos in ground_poses:
        x1,x2,y = pos
        clouds_map.append(Cloud_map(x1,x2,y))
#text_init
text_show = pygame.font.Font(None,50)
def text(body,v,color =little_blue):
    return text_show.render(str(body)+str(v),1,color)

def text_draw(role = role_1):
    role:Role
    draw(text("role1_pos: ",role.rect.center),(0,0))
    draw(text("role1_v: ",role.vx),(0,40))
    draw(text("role1_force: ",role.force_x),(0,80))
class Main:
    def __init__(self) -> None:
        self.main_init()
        self.mod_init()
    def mod_init(self):
        self.mods:function = [self.mod_none,self.mod_check_pos,self.mod_cloud]
        self.mod_status = 0
        self.cloud_length = 200

    def mod_none(self):
        pass
    def mod_update(self):
        if self.key == K_m:
            self.mod_status = 2
            print("now is cloud_edit_status")
        elif self.key == K_p:
            print("now is check_mouse_status")
            self.mod_status = 1
        elif self.key == K_q:
            print("now is common_status")
            self.mod_status = 0
        
        self.mods[self.mod_status]()

    def mod_cloud(self):
        if self.mouse_status == 4:
            self.cloud_length += 10
        elif self.mouse_status == 5:
            self.cloud_length -= 10
        x1,y = self.mouse_pos
        x2 = x1 + self.cloud_length
        cloud_followed = Cloud_map(x1,x2,y)
        draw(cloud_followed.cloud,self.mouse_pos)
        if self.mouse_down[0]:
            test_boxes.append(cloud_followed)
        if self.mouse_down[2]:
            if test_boxes:
                test_boxes.pop()

    def mod_check_pos(self):
        if self.mouse_status == 1:
            print(self.mouse_pos)
    
    def show_game_begin(self):
        pass
    def show_settings(self):
        pass
   
    def show_game(self):
        text_draw()
        self.screen_draw()
   
    def screen_draw(self):
        draw(background,self.background_rect.topleft)
        for ground_map in ground_maps:
            for ground in ground_map:
                ground.update()
        for role in role_group:
            role:Role
            role.update()
        for bullet in bullets:
            bullet:Bullet
            bullet.update()
    
    def main_init(self):
        self.screen_center = (SCREEN_LENGTH//2,SCREEN_WIDTH//2)
        self.background_rect = background.get_rect()
        self.background_center = (BACK_LENGTH//2,BACK_WIDTH//2)
        self.running =True
        self.main_update()
    def main_update(self):
        mouse_status = pygame.event.get(MOUSEBUTTONDOWN) 
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_status = mouse_status[0].button if mouse_status else 0
        self.mouse_down = pygame.mouse.get_pressed(5)
        self.press=pygame.key.get_pressed()
        key = pygame.event.get(KEYDOWN)
        self.key = key[0].key if key else 0
        self.mouse_pos = pygame.mouse.get_pos()

    def main(self):
        while self.running:
            self.main_update()
            if self.press[K_ESCAPE]:
                self.running = False
            self.show_game()
            self.mod_update()
            pygame.display.flip()
            pygame.time.Clock().tick(60)
# mod.append(mod_edit_maps)
if __name__ == "__main__":
    Main().main()

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