import random
import time
from tqdm import tqdm
#region mergefunc
def merge3(ls,l,r):
    n=r-l+1
    if n==1:
        return
    mid=(r+l)//2
    list1=ls[l:mid+1]
    list2=ls[mid+1:r+1]
    n1=len(list1)
    n2=len(list2)
    out_list=[]
    l1=l2=0
    while(l1<n1 and l2<n2):
        if list1[l1]>list2[l2]:
            out_list.append(list2[l2])
            l2+=1
        else:
            out_list.append(list1[l1])
            l1+=1
    if (l1==n1):
        out_list.extend(list2[l2:])
    else:
        out_list.extend(list1[l1:])
    for i in range(0,n):
        ls[l+i]=out_list[i]
def divid_sort3(ls:list,l:int,r:int):
    if l>=r:
        return
    mid=(l+r)//2
    divid_sort3(ls,l,mid)
    divid_sort3(ls,mid+1,r)
    merge3(ls,l,r)


def merge2(ls,l,r):
    if l>=r:
        return
    new_list=[0]*(r-l+1)
    mid = (r+l)//2
    p=0
    p1=l
    r_1=mid+1
    p2=r_1
    r_2=r+1
    while p1 != r_1 and p2 != r_2:
        if ls[p1] < ls[p2]:
            new_list[p]  = ls[p1]
            p1 += 1

        else:
            new_list[p]  = ls[p2]
            p2 += 1
        p += 1
    if p1 == r_1:
        while p2 != r+1:
            new_list[p] = ls[p2]
            p += 1
            p2 += 1
    else:
        while p1 != r_1:
            new_list[p] = ls[p1]
            p += 1
            p1 += 1
    for i in range(0,r-l+1):
        ls[l+i]=new_list[i]
def divid_sort2(ls,l,r):
    if l>=r:
        return 
    mid=(r+l)//2
    divid_sort2(ls,l,mid)
    divid_sort2(ls,mid+1,r)
    merge2(ls,l,r)


def merge(list1,list2):
    n1=len(list1)
    n2=len(list2)
    out_list=[]
    l1=l2=0
    while(l1<n1 and l2<n2):
        if list1[l1]>list2[l2]:
            out_list.append(list2[l2])
            l2+=1
        else:
            out_list.append(list1[l1])
            l1+=1
    if (l1==n1):
        out_list.extend(list2[l2:])
    else:
        out_list.extend(list1[l1:])
    return out_list
def divid_sort(l:list,r=1,s=1):
    n=len(l)
    if n==1:
        return l
    return merge(divid_sort(l[0:n//2]),divid_sort(l[n//2:]))

#endregion

def quicksort(ls,l,r):
    stack=[r,l]
    if l>=r:
        return
    pop=stack.pop
    push=stack.extend
    while stack:
        l,r=pop(-1),pop(-1)
        if l>=r:
            continue
        pivot_index=random.randint(l,r)
        ls[l],ls[pivot_index]=ls[pivot_index],ls[l]
        pivot = ls[l]
        pl=l+1
        pr=r
        while 1:
            while ls[pr]>pivot:
                pr-=1
            while pl<pr and ls[pl]<pivot:
                pl+=1
            if pl>=pr:
                break
            ls[pl],ls[pr]=ls[pr],ls[pl]
            pl+=1
            pr-=1
        ls[pr],ls[l]=ls[l],ls[pr]
        push([r,pr+1,pr-1,l])
#region finished_quick_sort
def quicksort5(ls,l,r):
    stack=[r,l]
    if l>=r:
        return
    pop=stack.pop
    push=stack.extend
    while stack:
        l,r=pop(-1),pop(-1)
        if l>=r:
            continue
        pivot_index=random.randint(l,r)
        ls[l],ls[pivot_index]=ls[pivot_index],ls[l]
        pivot = ls[l]
        pl=l+1
        pr=r
        while 1:
            while ls[pr]>pivot:
                pr-=1
            while pl<pr and ls[pl]<pivot:
                pl+=1
            if pl>=pr:
                break
            ls[pl],ls[pr]=ls[pr],ls[pl]
            pl+=1
            pr-=1
        ls[pr],ls[l]=ls[l],ls[pr]
        push([r,pr+1,pr-1,l])


def quicksort6(ls,l,r):
    if l>=r:
        return
    pivot=ls[l]
    pl = l
    pr = r
    while 1:
        while ls[pr]>pivot:
            pr-=1
        ls[pl]=ls[pr]
        while pl<pr and ls[pl]<pivot:
            pl+=1
        if pl>=pr:
            break
        ls[pr]=ls[pl]
        pr-=1
    ls[pl]=pivot
    quicksort6(ls,l,pl-1)
    quicksort6(ls,pl+1,r)


def quicksort4(ls,l,r):
    if l>=r:
        return
    pivot=ls[l]
    pl = l+1 
    pr = r
    while 1:
        while ls[pr]>pivot:
            pr-=1
        while pl<pr and ls[pl]<pivot:
            pl+=1
        if pl>=pr:
            break
        ls[pl],ls[pr]=ls[pr],ls[pl]
        pl+=1
        pr-=1
    ls[pr],ls[l]=ls[l],ls[pr]
    quicksort4(ls,l,pr-1)
    quicksort4(ls,pr+1,r)


def quicksort3(ls,l,r):
    if l>=r:
        return
    pivot_index=random.randint(l,r)
    pivot=ls[pivot_index]
    # pivot=ls[l]
    ls[pivot_index],ls[l]=ls[l],ls[pivot_index]
    pl = l+1 
    pr = r
    while 1:
        while ls[pr]>pivot:
            pr-=1
        while pl<pr and ls[pl]<pivot:
            pl+=1
        if pl>=pr:
            break
        ls[pl],ls[pr]=ls[pr],ls[pl]
        pl+=1
        pr-=1
    ls[pr],ls[l]=ls[l],ls[pr]
    quicksort3(ls,l,pr-1)
    quicksort3(ls,pr+1,r)


def quicksort1(ls:list,l,r):
    if r<=l:return 
    mid=ls[l]
    p=l
    for q in range(l+1,r+1):
        if ls[q]<mid:
            p+=1
            ls[p],ls[q]=ls[q],ls[p]
    ls[p],ls[l]=ls[l],ls[p]
    
    quicksort1(ls,l,p-1)
    quicksort1(ls,p+1,r)


def Mid(ls,l,r):
    mid=(l+r)//2
    if ls[l]>ls[mid]:
        ls[l],ls[mid]=ls[mid],ls[l]
    if ls[l]>ls[r]:
        ls[r],ls[l]=ls[l],ls[r]
    if ls[mid]>ls[r]:
        ls[r],ls[mid]=ls[mid],ls[r]
    ls[l+1],ls[mid]=ls[mid],ls[l+1]
    return ls[l+1]
def quicksort2(ls,l,r):
    if r<=l: return 
    pivot=Mid(ls,l,r)
    min_p,max_p=l+1,l+2
    while max_p<r:
        if ls[max_p]<=pivot:
            min_p+=1
            ls[min_p],ls[max_p]=ls[max_p],ls[min_p]
        max_p+=1
    ls[min_p],ls[l+1]=ls[l+1],ls[min_p]
    quicksort2(ls,l,min_p-1)
    quicksort2(ls,min_p+1,r)
#endregion

ls=[]
get_time = time.time

test_num = 10000#测试数据量
is_print_ls=True
is_print_ls=False
is_print_time=True
is_print_time=False
is_print_cmp=True
is_print_cmp=False
is_print_res=True
is_print_res=False
running_times=100
for _ in range(test_num):
    ls.append(random.randint(1,100))
l ,r = 0 , len(ls)-1
"""
3 2 5 

1 2 3 5
2 4 6 8

4

"""
# ls.sort(
func_list = [ 
    # quicksort,
    quicksort4,
    # quicksort3,
    quicksort6,
    # divid_sort,
    # divid_sort2,
    # divid_sort3,
]
mp={}
for i in range(len(func_list)):
    mp[i]=0

for _ in tqdm(range(running_times),desc="Process0"):
    cmp=[] 
    for func in func_list:
        copy_list=ls.copy()
        start=get_time()
        func(copy_list,l,r)
        end = get_time()
        cmp.append(end-start)
        if is_print_ls:
            print(ls)
        if is_print_cmp:
            print(copy_list.__eq__(sorted(ls)))
            # sw=(cop)
        if is_print_time:
            print(end-start)
        if is_print_res:
           print(copy_list)
    mp[cmp.index(min(cmp))]+=1
for key,value in mp.items():
    print(func_list[key].__name__,value)