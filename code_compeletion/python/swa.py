# a=int(input())
# t=[]
# for _ in range(a):
#     s=input()
#     count=1
#     l=set()
#     for j in s:
#         if j in l:
#             count+=1
#         l.add(j)
#     if count==3:
#         t.append("Yes")
#     else:t.append("No") 
# for i in range(len(t)):
#   print(t[i],end="")
#   if i!=len(t)-1:
#     print("\n",end="")
import os
import sys
def s(i:int,a:str):
  res=0
  if a=="R":
    res=i*2
  else:res=i*2-1
  return res
# 请在此输入您的代码
a,b=map(int,input().split())
for _ in range(b):
    init=1
    pd=input()
    for i in pd:
        init=s(init,i)
    print(init)
