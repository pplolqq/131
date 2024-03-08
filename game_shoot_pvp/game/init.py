import pygame
from pygame.locals import *
import random
import math
from constants import *
pygame.init()

# DIFFER_X= (BACK_LENGTH - SCREEN_LENGTH)//2
# DIFFER_Y= (BACK_WIDTH - SCREEN_WIDTH)//2
screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))
pygame.display.set_caption("shoot_pvp")

def point_add(p, q):
    return (p[0] + q[0], p[1] + q[1])
def point_minus(p, q):
    return (p[0] - q[0], p[1] - q[1])

pic = pygame.image.load
draw = screen.blit
get_time = pygame.time.get_ticks

background = pic(r"game_shoot_pvp\pic\back1.png")
cloud_init = pic(r"game_shoot_pvp\pic\cloud.png")
bullets = []
ground_maps = []
clouds_map = []
test_boxes = []
ground_maps.append(clouds_map)
ground_maps.append(test_boxes)
player_total = 2
# ground_poses1=[[165, 345, 200], [440, 580, 180], [680, 850, 175], [265, 740, 250], [165, 326, 350], [370, 600, 350], [680, 870, 330],[780,885,235]]
ground_poses = [[105, 335, 210], [10, 240, 270], [160, 450, 335], [705, 935, 210], [800, 1030, 270], [590, 880, 335], [310, 730, 270]]


def slope_calculate(p1: tuple[int,int],p2: tuple[int,int]):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    if dx :
        return int(dy/dx*1000)
    else:
        if dx >0:
            return 600
        else:
            return -1000


color_selected = [green,orange]


"""
抛物线方程
y = -1*(400-x) * x // 1000


"""


"""
键盘读取
kr_select = []
        for idx,bool in enumerate(pygame.key.get_pressed()):
            if bool :
                kr_select.append(idx) if idx not in kr_select else ""
                break

"""