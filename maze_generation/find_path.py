"""
给出最短的寻路算法

自动移动

"""

"""
bfs
"""
def path_(mp:list[list[int]],start_pos=[1,1]):
    m,n = len(mp),len(mp[0])
    res = []
    ans = [start_pos]
    record = [x.copy() for x in mp]
    dir_move = [(1,0),(-1,0),(0,1),(0,-1)]
    record[start_pos[0]][start_pos[1]] = 0
    def bfs(i=start_pos[0],j=start_pos[1]):
        if i>=m or j>=n:
            return
        if i==m-2 and j==n-2:
            res.append(ans.copy())
            return
        for dir in dir_move:
            x = i+dir[0]
            y = j+dir[1]
            if record[x][y]:
                record[x][y] = 0
                ans.append([x,y])
                bfs(x,y)
                record[x][y] = 1
                ans.pop()
    bfs()
    return res[0] if res else []
if __name__ == "__main__":
    from creat import creat
    m,n = 5,5
    mp = creat(m,n)
    start_pos = []
    for i in range(2*m+1):
        if start_pos:
            break
        for j in range(2*n+1):
            if mp[i][j]==1 and not start_pos:
                start_pos = [i,j]
                break
    print(start_pos)
    # for i in mp:
    #     print(i)
    res = path_(mp,start_pos)
    # print(res[0])
    print(res)