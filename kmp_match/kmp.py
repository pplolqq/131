def max_repeat_array(str:str):
    n=len(str)
    idx=1
    pc=0
    arr=[0]*n
    # ABABA
    for idx in range(1,n):
        v=str[idx]
        while pc and str[pc] != v:
            pc=arr[pc-1]
        if v==str[pc]:
            pc+=1
        arr[idx]=pc
    # while idx<n:
    #     if str[pc]==str[idx]:
    #         pc+=1
    #         arr[idx]=pc
    #         idx+=1
    #     else:
    #         if pc!=0:
    #             pc=arr[pc-1]
    #         else:
    #             arr[idx]=0
    #             idx+=1
    return arr
def match_two_string(str,mat):
    arr=max_repeat_array(mat)
    p1=p2=0
    n1=len(str)
    n2=len(mat)
    l=[]
    while(p1<n1):
        if str[p1]==mat[p2]:
            p1+=1
            p2+=1
        else:
            if p2==0:
                p1+=1
            else:
                p2=arr[p2-1]
        if p2==n2:
            l.append(p1-p2)
            p2=arr[p2-1]
            # return p1-p2
    return l
def divide(arr,target):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if target>arr[mid]:
            l=mid+1
        else:
            r=mid-1
    return l
str="AAAABB"
match="AB"
A="ababababazzabababb"
B="aba"
C="squirrel"
ans1=match_two_string(A,B)
ans2=match_two_string(A,C)
print(ans1)
print(ans2)