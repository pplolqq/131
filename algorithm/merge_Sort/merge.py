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
def divid_sort(l:list):
    n=len(l)
    if n==1:
        return l
    return merge(divid_sort(l[0:n//2]),divid_sort(l[n//2:]))
l1=[1,5,7,10,1,1,4]
print(divid_sort(l1))