from Role import *



def Role_img(color):
    return pic(r"game_shoot_pvp\pic\role_{}.png".format(color))
Kr_player1 = Kr(K_w,K_a,K_d,K_s,K_j)
Kr_player2 = Kr(K_UP,K_LEFT,K_RIGHT,K_DOWN,K_KP_1)

role_1 = Role(Role_img("green"),Kr_player1,0)
role_2 = Role(Role_img("orange"),Kr_player2,1)

role_group = [role_1,role_2]

text_show = pygame.font.Font(None,50)
little_blue = (0,200,255)

def text(body,v,color =little_blue):
    return text_show.render(str(body)+str(v),1,color)
def text_draw(role = role_1):
    draw(text("role1_pos: ",role.rect.center),(0,0))
    draw(text("role1_v: ",role.vx),(0,40))
    draw(text("role1_force: ",role.force_x),(0,80))

work_pos = [(100+x*40,0) for x in range(3)]

def draw_line(startpos,endpos,wide=5,color=green):
    pygame.draw.line(screen,color,startpos,endpos,wide)

def main():
    running =True
    
    while running:
        press=pygame.key.get_pressed()
        for even in pygame.event.get():
            if even.type == QUIT:
                running = False
            if even.type == MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        if press[K_ESCAPE]:
            running = False
        draw(background,(0,0))
        draw(map1,(150,150))
        # for ground in ground_poses:
            # pygame.draw.line(screen,(255,0,0),(ground[0],ground[2]),(ground[1],ground[2]),5)
        
        for role in role_group:
            role:Role
            role.update()
        for bullet in bullets:
            bullet:Bullet
            bullet.update()
        
        text_draw()
        pygame.display.flip()
        pygame.time.Clock().tick(60)
if __name__ == "__main__":
    main()
    
