import random

from Init import *
from Plants import Plant
from Zombie import Zombie

# plants_pos = [(150, 10),(225, 10)]
cards_pos = [(75 * i + 150, 10) for i in range(SLOT_NUM)]

plants_cooldown_time = {PEE: 2000, SUNFLOWER: 3000}




def intersect(pos, rect):
    x = pos[0] - rect.left
    y = pos[1] - rect.top
    return 0 <= x <= rect.width and 0 <= y <= rect.height



class Plant_Slot:
    def plant_slot_init(self, selected_plants):
        new_plants = []
        for num, id in enumerate(selected_plants):
            new_plants.append(Plant_Card(num, id))
        return new_plants

    def __init__(self, selected_plants):
        self.selected_plants = self.plant_slot_init(selected_plants)
        self.is_follow = False
        self.generate_time = get_time()
        
        self.is_clicked = False
        self.follow_plant = None
    def update(self):

        self.zombie_generate()
        if self.is_clicked:
            self.is_clicked = self.follow_plant.is_follow
        else:
            self.check_click()

    def check_click(self):
        now_time = get_time()
        mouse_pos = get_mouse_pos()
        mouse_press = pygame.mouse.get_pressed(3)
        for plant in self.selected_plants :
            plant: Plant_Card
            if mouse_press[0] and intersect(mouse_pos,plant.rect) and not plant.is_cooldown:
                self.is_clicked = True
                self.follow_plant = plant
                plant.is_follow = True
                plant.follow_start = now_time
                plant.card_image = plant.card_cd


    def zombie_generate(self):
        now_time = get_time()
        zombie_row = random.randint(0, RAW_NUM - 1)
        if now_time - self.generate_time >= 10000 or pygame.key.get_pressed()[K_a]:
            self.generate_time = now_time
            zombies_pool[zombie_row].append(Zombie(zombie_row))


class Plant_Card:
    def __init__(self, num, id):
        self.pos = cards_pos[num]
        self.id = id
        self.__common(id)
        self.__attrs()

    def __common(self, id):
        self.card_image = pic(pic_set[id].card)
        self.card_image1 =self.card_image
        self.card_cd = pic(pic_set[id].cd)
        self.rect = self.card_image.get_rect()
        self.rect.topleft = self.pos
        self.cool_time = plants_cooldown_time[id]
        self.follow_img = pic(pic_set[id].img)
        self.followpos = self.follow_img.get_rect()
        self.trans_img = pic(pic_set[id].tpr)
        self.transpos = self.trans_img.get_rect()

    def __attrs(self):
        self.is_cooldown = False
        self.is_follow = False
        self.follow_start = 0
        self.cooldown_start = 0

    def check_cooldown(self):
        if self.is_cooldown:
            self.cooldown()

    def cooldown(self):
        dt = get_time() - self.cooldown_start
        interval = self.cool_time // self.rect.height
        posy = self.rect.height - dt // interval  #
        if posy < 0:
            self.is_cooldown = False
            return
        black = pygame.Surface((self.rect.width, posy))
        black.blit(self.card_cd, (0, 0))
        draw(black, self.pos)

    def check_follow(self):
        if self.is_follow:
            self.follow()
        else:
            self.card_image = self.card_image1
    def follow(self):
        mouse_pos = get_mouse_pos()
        self.followpos.center = mouse_pos
        mouse_status = pygame.mouse.get_pressed(3)
        pos_res = pos_to_grass_calculator(mouse_pos)
        is_pos_to_plant = pos_res[0] 
        if mouse_status[2]:
            self.is_cooldown = False
            self.is_follow = False
            return False
        if  is_pos_to_plant:
            r, c = pos_res[1]
            self.transpos.center = grass_pos[r][c]
            draw(self.trans_img, self.transpos.topleft)
            now_time = get_time()
            if now_time - self.follow_start >= 100 and mouse_status[0] : 
                    self.cooldown_start = now_time
                    self.is_cooldown = True
                    self.is_follow = False
                    plants_pos[r][c] = self.generate((r,c))
                    return False
            
        draw(self.follow_img, self.followpos.topleft)
        return True
   

    def update(self):
        draw(self.card_image, self.rect.topleft)

        self.check_follow()
        self.check_cooldown()

    def generate(self, pos_dot):
        return Plant(self.id, pos_dot)

