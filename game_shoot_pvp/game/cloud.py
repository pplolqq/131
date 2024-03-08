from init import *
cloud_width = 40

class Map_ground():
    def __init__(self) -> None:
        self.rect:pygame.Rect
class Cloud_map(Map_ground):
    def __init__(self,x1,x2,y,color=red) -> None:
        self.length = x2 - x1
        self.color = color 
        self.pos = (x1,y)
        y += 20
        self.rect = pygame.draw.aaline(screen,self.color,(x1,y),(x2,y),5)
        self.cloud = pygame.transform.scale(cloud_init,(self.length,cloud_width))
    def update(self):
        # pygame.draw.rect(screen,self.color,self.rect,5)
        draw(self.cloud,self.pos)