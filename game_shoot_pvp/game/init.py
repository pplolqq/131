import pygame
from pygame.locals import *
import random
import math
pygame.init()
SCREEN_LENGTH = 1000
SCREEN_WIDTH = 600
screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))
pygame.display.set_caption("shoot_pvp")

pic = pygame.image.load
draw = screen.blit
get_time = pygame.time.get_ticks

background = pic(r"game_shoot_pvp\pic\back1.png")
map1 = pic(r"game_shoot_pvp\pic\map1.png")

bullets = []

def point_add(p, q):
    return (p[0] + q[0], p[1] + q[1])
def point_minus(p, q):
    return (p[0] - q[0], p[1] - q[1])

player_total = 2

ground_poses=[[165, 345, 200], [440, 580, 180], [680, 850, 175], [265, 740, 250], [165, 326, 350], [370, 600, 350], [680, 870, 330],[780,885,235]]


# print(rotato_pos1)
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
orange = (255,125,40)
green = (180,230,30)
white = (255,255,255)

color_selected = [green,orange]

GRAVITY = 1
PLAYER_MOVE_SPEED = 10
JUMP_SPEED = 12

BULLET_SPEED = 30


ROLE_LENGTH = 50
ROLE_WIDTH = 50