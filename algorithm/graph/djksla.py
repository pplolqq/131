m,n,num=map(int,input().split(" "))
m,n,num=3,3,3
l=[[] for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split(" "))
    l[x].append(y)
    l[y].append(x)
def search(x,y,onpath):
    for i in l[x]:
        if(onpath[i]==0):
            continue
        if i==y:
            return True
        else:
            onpath[x]=0
            if search(i,y,onpath):
                return True
    return False