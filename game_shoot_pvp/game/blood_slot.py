from init import *


class Blood_slot:
    def __init__(self,color,pos):
        self.text_style = pygame.font.Font(None,50)

        self.pos = pos 
    
        self.border_color = (255,255,255)

        rect_border = 5

        self.pos_rect = self.pos
        self.l_w_rect = (160,50)
        
        self.pos_rect_back = point_add(self.pos_rect,(rect_border,rect_border))
        self.l_w_rect_back = (50,50)

        self.pos_role = point_add(self.pos_rect,(rect_border,rect_border))
        self.l_w_role = point_minus(self.l_w_rect_back,(2*rect_border,2*rect_border))
        self.role_color = color

        self.pos_blood_slot = point_add(self.pos_rect, (-20,50))
        self.l_w_blood_slot = (200,50)

        self.pos_blood_back = point_add(self.pos_blood_slot,(rect_border,rect_border))
        self.l_w_blood_back = point_minus(self.l_w_blood_slot,(2*rect_border,2*rect_border))
        self.blood_back_color = (125,125,125) #灰色

        self.pos_blood = self.pos_blood_back
        self.l_w_blood = self.l_w_blood_back
        
        self.blood_length = 190
        self.length = self.blood_length
        self.blood_color = (0,255,0) #绿色

        self.lives = 15
        self.text = self.text_style.render(str(self.lives),True,(255,255,255))

    def text_update(self):
        self.lives -= 1
        self.length = self.blood_length
        self.text = self.text_style.render(str(self.lives),True,(255,255,255))   
    def update(self):
        self.l_w_blood = (self.length,40)
        pygame.draw.rect(screen,self.border_color,pygame.Rect(self.pos_rect,self.l_w_rect),5)
        pygame.draw.rect(screen,self.border_color,pygame.Rect(self.pos_rect,self.l_w_rect_back),5)
        pygame.draw.rect(screen,self.role_color,pygame.Rect(self.pos_role,self.l_w_role),0)
        pygame.draw.rect(screen,self.blood_back_color,pygame.Rect(self.pos_blood_back,self.l_w_blood_back),0,10)
        pygame.draw.rect(screen,self.blood_color,pygame.Rect(self.pos_blood,self.l_w_blood),0,10)
        pygame.draw.rect(screen,self.border_color,pygame.Rect(self.pos_blood_slot,self.l_w_blood_slot),5,20)
        draw(self.text,(self.pos_role[0]+60,self.pos_role[1]+5))
