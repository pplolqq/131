import pygame
from constants import *
from pygame.locals import *



class Date:
    def __init__(self):
        self.now_time = 0
        self.mouse_pos = (0, 0)

    def update_data(self):
        self.now_time = pygame.time.get_ticks()
        self.mouse_pos = pygame.mouse.get_pos()

    def get_time(self):
        return self.now_time

    def get_mouse_pos(self):
        return self.mouse_pos


date = Date()
"""

初始化数值在各函数与类之间的传递问题 ..ok
时间调用函数太过频繁   ... ok
对象池过多
公有类的实现


设计模式太过低级
"""
pygame.init()
SCREEN_LENGTH = 1000
SCREEN_WIDTH = 600
screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))
pygame.display.set_caption("pvz")
# region 一些缩写
pic = pygame.image.load
draw = screen.blit
get_time = date.get_time
get_mouse_pos = date.get_mouse_pos


# endregion


def background_init():
    return pic(r"C:\python.pycharm\picture\pic\background\background1.jpg")  # 1400 800


def slot_init():
    return pic(r"C:\python.pycharm\picture\pic\background\toolbar.png")  # 600 105


# 场景初始化
background = background_init()
slot = slot_init()

grass_pos = [[(x * 80 + 95, y * 100 + 110) for x in range(COLUMN_NUM)] for y in range(RAW_NUM)]


def pos_to_grass_calculator(pos):
    r = round((pos[1] - 110) / 100)
    c = round((pos[0] - 95) / 80)
    if 0 <= r <= RAW_NUM - 1 and 0 <= c <= COLUMN_NUM - 1 and not plants_pos[r][c]:
        return [True, (r, c)]
    else:
        return [False]


plants_pos = [[None] * COLUMN_NUM for _ in range(RAW_NUM)]

zombies_pool = [[] for _ in range(RAW_NUM)]


class Pic_Path:
    def __init__(self, info):
        plant_name = info[0]
        gif_num = info[1]
        self.path = r"C:\python.pycharm\picture\pic_plant\{}".format(plant_name)
        self.img = self.path + r"\img.png"
        self.card = self.path + r"\card.png"
        self.cd = self.path + r"\card_cd.png"
        self.tpr = self.path + r"\card_tpr.png"
        self.gif = [self.path + r'\gif\No{}.png'.format(i) for i in range(gif_num)]


NAME = 0
NUMBER = 1
pee_info = ["pee", 13]
sunflower_info = ["sunflower", 18]
info_set = {
    PEE: pee_info,
    SUNFLOWER: sunflower_info
}
pic_set = {
    SUNFLOWER: Pic_Path(sunflower_info),
    PEE: Pic_Path(pee_info)
}
if __name__ == "__main__":
    pass
