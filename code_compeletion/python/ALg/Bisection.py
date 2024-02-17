import time
def Bisection(ls:list,a:int):#l is under_ordered
    r=len(ls)
    l=0
    mid=l+(r-l>>1)
    while mid!=l:
        if a==ls[mid]:
            break
        elif a>ls[mid]:
            l=mid
            mid=l+(r-l>>1)
        elif a<ls[mid]:
            r=mid
            mid=l+(r-l>>1)
    return mid
def Bisection2(ls:list,a:int):
    if a<ls[0]:
        return 0
    elif a>ls[-1]:
        return len(a)
    l=0
    r=len(ls)-1
    mid=l+(r-l)>>1
    while r>l:
        if a>=ls[mid] :
            l=mid
            mid=l+(r-l>>1)
        elif a<ls[mid]:
            r=mid
            mid=l+(r-l>>1)
        else:
            return mid
    return l if a in l else r
        
a=3
l=[1,2,3,6,7,8,9,10]
print(Bisection2(l,a))
print(1+(3-1>>1))
# if q:=l[0:0]==[]:
    # print(22)
# if 1>0:
#     print(6)
# # print(1)
# for i in range(2):
#     print(1)
# else:
# #     print(2)
# import t
# print(t.k)
def weigh_sum(l):
    j=1
    sum=0
    for i in l:
        sum+=j*i
        j+=1
    print(sum)
# weigh_sum([1,2,3,4])
