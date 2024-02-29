import sys

from Init import *

from Plants_slot import Plant_Slot

from Zombie import  Zombie

from Sun import sun
z=Zombie(2)

selected_plants = [SUNFLOWER, PEE]
Slot = Plant_Slot(selected_plants)
update_lists = [
    Slot.selected_plants
]

def update(update_lists):
    for update_list in update_lists:
        for role in update_list:
            role.update()

def game_draw():
    draw(background, (-200, 0))
    draw(slot, (50, 0))
    update(update_lists)
    for raw in plants_pos:
        for plant in raw:
            if plant:
                plant.update()
    for raw in zombies_pool:
        for zombie in raw:
            zombie.update()
    Slot.update()
    

def exit_game():
    pygame.quit()
    sys.exit()

def main():
    while 1:
        date.update_data()
        press = pygame.key.get_pressed()
        for even in pygame.event.get():
            if even.type == QUIT:
                exit_game()
            if even.type == MOUSEBUTTONDOWN:
                print(get_mouse_pos())
        if press[K_ESCAPE]:
            exit_game()
        game_draw()
        pygame.display.flip()
        pygame.time.Clock().tick(60)


if __name__ == "__main__":
    main()
