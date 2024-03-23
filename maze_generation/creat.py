import random
def creat(m,n):
    """
    生成一个 高 2m-1 宽 2n-1 的迷宫
    （外围是墙） 
    """

    """
    valid -> chose and record -> connect_record
    invalid -> pop
    record -> x,y add and mp[x][y]=2
    connect -> pos nextpos -> mid =2
    
    """
    mp = [[1 if x%2 and y%2 else 0 for y in range(2*n+1)] for x in range(m*2+1)]
    dir_move = [[2,0],[-2,0],[0,-2],[0,2]] #上下左右
    x,y = (random.randint(1,m),random.randint(1,n))
    pos = [2*x-1,2*y-1]
    start_pos = [2*x-1,2*y-1]
    stack_pos = [pos]
    mp[2*x-1][2*y-1] = 2
    while stack_pos:
        pos = stack_pos[-1]
        pos_chosen = []
        for i in range(4):
            move = dir_move[i]
            x,y = pos[0]+move[0],pos[1]+move[1]
            if 1<=x<=2*m-1 and 1<=y<=2*n-1 and mp[x][y] == 1:
                pos_chosen.append([x,y])
        if pos_chosen:    #valid 判断
            next_pos = random.choice(pos_chosen)
            stack_pos.append(next_pos)  #add
            x,y = next_pos
            mp[x][y] = 2  #nextpos 标记
            x,y = connect(pos,next_pos)
            mp[x][y] = 2  #nextpos 与 pos 之间的点标记
        else:
            stack_pos.pop()
    mp[start_pos[0]][start_pos[1]] = 1
    mp[-2][-2] = 1
    return mp
def connect(pos1,pos2):
    x = (pos1[0]+pos2[0])//2
    y = (pos1[1]+pos2[1])//2
    return [x,y]
if __name__ == '__main__':
    mp = creat(3,3)
    for i in mp:
        print(i)
    pass
    

















