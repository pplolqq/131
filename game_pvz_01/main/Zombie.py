from Init import *

path = [pic(r"C:\python.pycharm\picture\pic\gif\gif_zombie\No{}.png".format(i)) for i in range(31)]
rows = [100 * i + 80 for i in range(RAW_NUM)]

def pos_block(pos_x):
    c = round((pos_x - 95) / 80)
    if 0<=c<=COLUMN_NUM-1:
        return [True,c]
    return [False,0]

class Zombie:
    def __init__(self, row):
        self.row = row
        self.img_num = 0
        self.img = path[self.img_num]
        self.rect = self.img.get_rect()
        self.rect.center = (800, rows[row])
        self.gif_update_time = get_time()
        self.move_speed=1

    def gif(self):
        now_time = get_time()
        if now_time - self.gif_update_time >= 100:
            self.gif_update_time = now_time
            self.img_num += 1
            self.img_num %= 31
            self.move()
            self.img = path[self.img_num]

    def move(self):
        self.rect.centerx-=self.move_speed

    def eat(self):
        is_ok_eat=pos_block(self.rect.centerx)
        column=is_ok_eat[1]
        if is_ok_eat[0]:
            if plants_pos[self.row][column]:
                self.move_speed = 0
                plants_pos[self.row][column]=None
            else:
                self.move_speed=1
    def set_blood(self):
        pass

    def update(self):
        self.gif()
        self.eat()
        draw(self.img, self.rect.topleft)
