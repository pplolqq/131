n,total=list(map(int,input().split(" ")))
va=[]
vw=[]
for i in range(n):
    m,v=list(map(int,input().split(" ")))
    vw.append(m)
    va.append(v)
def dfs(sum:int,i):
    if i<0 or sum<0:
        return 0
    return max(dfs(sum,i-1),dfs(sum-vw[i],i-1)+va[i])
print(dfs(total,n-1))
"""
4 50
10 60
20 100
30 120
15 45
"""