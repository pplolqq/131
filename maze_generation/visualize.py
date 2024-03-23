import pygame
from creat import creat
from find_path import path_
pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Auto_Maze")
running = True
SIZE = 20
m,n = (SCREEN_HEIGHT//SIZE-1)//2,(SCREEN_WIDTH//SIZE-1)//2


class Block:
    def __init__(self,color,x,y) -> None:
        self.x,self.y = x,y
        self.color = color 
    def update(self):
        self.rect = pygame.draw.rect(screen,self.color,(self.y*SIZE,self.x*SIZE,SIZE,SIZE))

wall_color = (50,30,90)
red = (255,0,0)
path_color = (255,255,255)


class Role:
    def __init__(self,start_pos,track_path,mp) -> None:
        self.start_pos:list[int] = start_pos
        self.track_path:list[list[int]] = track_path
        self.mp:list[list[int]] = mp
        self.x = start_pos[1]
        self.y = start_pos[0]
        self.pos = (SIZE*self.x,SIZE*self.y)
        self.img = pygame.image.load(r"maze_generation\role.png")
        self.img = pygame.transform.scale(self.img,(SIZE//2,SIZE//2))
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
        self.dirmove = [(1,0),(-1,0),(0,1),(0,-1)]
        self.move_a = False
        self.move_d = False
        self.move_w = False
        self.move_s = False
        self.idx = 0
    def target(self):
        """
        模拟人物移动
        实现自动化
        """
        self.move_a,self.move_d,self.move_s,self.move_w = False,False,False,False
        if self.idx==len(self.track_path):
            return
        c = self.rect.centerx//SIZE
        r = self.rect.centery//SIZE
        dc = c - self.track_path[self.idx][1]
        dr = r - self.track_path[self.idx][0]
        if dc==0 and dr ==0:
            self.idx +=1
            return
        if dc <0:
            self.move_d = True
        elif dc >0:
            self.move_a= True
        if dr < 0:
            self.move_s = True
        elif dr >0:
            self.move_w = True
    def update(self):
        self.target()
        press = pygame.key.get_pressed()
        v = 5
        """
        双向分治
        优化移动
        """
        self.x = self.rect.centerx//SIZE
        self.y = self.rect.centery//SIZE
        if press[pygame.K_a] or self.move_a:
            self.rect.x -=v
        if press[pygame.K_d] or self.move_d:
            self.rect.x +=v
        for dir in self.dirmove :
            x = self.x+dir[0]
            y = self.y+dir[1]
            if not (0<=x<=2*n and 0<=y<=2*m):
                continue
            if not self.mp[y][x] and self.rect.colliderect(pygame.Rect(x*SIZE,y*SIZE,SIZE,SIZE)):
                self.rect.x -= v*dir[0]
                self.rect.y -= v*dir[1]
                break
        self.x = self.rect.centerx//SIZE
        self.y = self.rect.centery//SIZE
        if press[pygame.K_w] or self.move_w:
            self.rect.y -=v
        if press[pygame.K_s] or self.move_s:
            self.rect.y +=v
        for dir in self.dirmove:
            x = self.x+dir[0]
            y = self.y+dir[1]
            if not (0<=x<=2*n and 0<=y<=2*m):
                continue
            if not self.mp[y][x] and self.rect.colliderect(pygame.Rect(x*SIZE,y*SIZE,SIZE,SIZE)):
                self.rect.x -= v*dir[0]
                self.rect.y -= v*dir[1]
                break
        if pygame.mouse.get_pressed()[0]:
            print(self.y,self.x)
            print(self.idx)
        screen.blit(self.img,self.rect.topleft)
class Auto_Maze_Trace:
    def __init__(self) -> None:
        self.running = True
        self.blocks = []
        self.mp = []
        self.start_pos = [],
        self.track_path = []
        self.m,self.n = m,n
        self.role:Role
        self.generate()
    def generate(self):
        self.mp = creat(self.m,self.n)
        self.blocks = []
        self.start_pos = []
        for i in range(2*m+1):
            for j in range(2*n+1):
                if self.mp[i][j] == 2:
                    self.blocks.append(Block(path_color,i,j))
                elif self.mp[i][j] == 1:
                    if not self.start_pos:
                        self.start_pos = [i,j]
                    self.blocks.append(Block(red,i,j))
                else:
                    self.blocks.append(Block(wall_color,i,j))
        self.track_path = path_(self.mp,self.start_pos)
        self.role = Role(self.start_pos,self.track_path,self.mp)
    def main(self):
        while self.running:
            press = pygame.key.get_pressed()
            for _ in pygame.event.get():
                continue
            if press[pygame.K_ESCAPE]:
                self.running = False
            screen.fill((0,0,0))
            for block in self.blocks :
                block:Block
                block.update()
            if self.role.idx == len(self.track_path):
                self.generate()
            self.role.update()
            pygame.display.flip()
            pygame.time.Clock().tick(60)


if __name__ == "__main__":
    Auto_Maze_Trace().main()