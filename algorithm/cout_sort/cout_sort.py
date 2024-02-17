# def f(x,n):
#     while(n):
#         x//=10
#         n-=1
#     return x%10
# def cout_sort(l,n):
#     m=[0]*(10)
#     for i in l:
#         m[f(i,n)]+=1
#     for i in range(1,10):
#         m[i]=m[i-1]+m[i]
#     s=[0]*len(l)
#     for i in range(len(l)-1,-1,-1):
#         t=l[i]
#         x=f(t,n)
#         s[m[x]-1]=t
#         m[x]-=1
#     return s
# l=[int ( i) for i in "24 12 2 18 8 34 22 6 40 30 32 16 36 14 8 38 10 28 26 20 \
# 16 34 24 40 18 10 32 2 20 8 38 6 28 22 4 26 8 14 36 30 \
# 6 10 16 20 40 8 38 24 30 4 26 2 14 32 12 36 18 22 28 8 \
# 2 8 6 30 20 18 26 16 8 12 36 24 22 38 34 28 40 32 14 4 \
# 24 18 2 8 30 40 36 6 4 34 28 16 32 26 10 14 20 38 22 12 \
# 16 40 24 4 8 20 28 2 12 10 14 6 38 36 8 22 30 26 32 34".split(" ")]
# l=cout_sort(l,0)
# l=cout_sort(l,1)
# l=cout_sort(l,2)
# print(l)
def trans(x,n):
    while(n):
        x/=10
        n-=1
    return x%10
def cout_sort(l,n):
    cout_list=[0]*10
    for i in l:
        cout_list[trans(i,n)]+=1
    for i in range(1,10):
        cout_list[i]=cout_list[i-1]+cout_list[i]
    s=[0]*len(l)
    for i in range(len(l)-1,-1,-1):
        t=l[i]
        x=trans(t,n)
        s[cout_list[x]-1]=t
        cout_list[x]-=1
    return s
print(cout_sort([1,2,4,2,1],0))
        

        

