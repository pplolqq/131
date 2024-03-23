import random
def creat(m,n):
    """
    select ->valid
    is_valid ->mark_ok -> find -> add new
    dis_valid -> mark_false -> pop
    
    """
    mp = [[1 if x%2 and y%2 else 0 for y in range(2*n+1)] for x in range(m*2+1)]
    dir_move = [[1,0],[-1,0],[0,-1],[0,1]] #上下左右
    zero_stack = []
    x,y = random.randint(1,m),random.randint(1,n)
    pos = [2*x-1,2*y-1]
    mp[2*x-1][2*y-1] = 2
    start_pos = [2*x-1,2*y-1]
    for dir in dir_move:
        x = pos[0]+dir[0]
        y = pos[1]+dir[1]
        if 1<=x<=2*m-1 and 1<=y<=2*n-1:
            zero_stack.append([x,y])
    while zero_stack:
        zero_pos = random.choice(zero_stack)
        zero_stack.remove(zero_pos)
        pos = []
        for dir in dir_move:
            x,y = zero_pos[0]+dir[0],zero_pos[1]+dir[1]
            if mp[x][y] == 1:
                pos = [x,y]
                mp[x][y] = 2
                mp[zero_pos[0]][zero_pos[1]] = 2
        if pos:
            for dir in dir_move:
                x = pos[0]+dir[0]
                y = pos[1]+dir[1]
                if 1<=x<=2*m-1 and 1<=y<=2*n-1 and not mp[x][y]:
                    zero_stack.append([x,y])
    mp[start_pos[0]][start_pos[1]] = 1
    mp[-2][-2] = 1
    return mp
if __name__ == "__main__":
    mp = creat(3,3)
    for i in mp:
        print(i)