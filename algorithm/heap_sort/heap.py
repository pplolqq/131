#wait to improve


class Root:
    def __init__(self,val,lnode=None,rnode=None):
        self.lnode=lnode
        self.rnode=rnode
        self.val=val

def Findroot(root:Root,val):
    temp=root
    while temp:
        findroot=temp
        if val>temp.val:
            temp=temp.rnode
        else:
            temp=temp.lnode
    return findroot

def Rangetree(root):
    if root is None:
        return       
    Rangetree(root.lnode)
    Rangetree(root.rnode)
    print(root.val)

def generatetree(root:Root,val):
    if root is None:
        return Root(val)
    findroot=Findroot(root,val)
    if(val>findroot.val):findroot.rnode=Root(val)
    else:findroot.lnode=Root(val)
    return root
root=None
l=[3,1,4,2,5,6]
for i in l:
    root=generatetree(root,i)

# Rangetree(root)
# def check(root,num):
#     t=Findroot(root,num)
#     if t.rnode == num or t.lnode==:
