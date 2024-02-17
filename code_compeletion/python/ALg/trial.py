class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res=""
        l_1=[]
        if s.count("1")<=k-1:
            return res
        lf=0
        for i ,m in enumerate(s):
            if m=="1":
                l_1.append(i)
                if len(l_1)==k:
                    res=s[l_1[0]:l_1[-1]+1]
                if len(l_1)>k:
                    o=s[l_1[-k]:i+1]
                    if len(o)<len(res):
                        res=o
                    elif len(o)==len(res) and o<res:
                        res=o

        return res
    def minimumSum(self, nums: list[int]) -> int:
        n=len(nums)
        a=3*10**8+1
        res=a
        # l_min=nums[0]
        # r_min=nums[-1]
        l=[0]*n
        l[-1]=nums[-1]
        for i in range(n-2,1,-1):
            l[i]=min(l[i+1],nums[i]) 
        pre=nums[0]
        for i in range(1,n-1):
            suf=l[i+1]
            print(suf)
            if suf< nums[i] and nums[i]>pre:
                res=min(res,nums[i]+pre+suf)
            pre=min(pre,nums[i])
        # print(res)
        return res if res!=a else -1
# s="110101000010110101"
# k=3
# print(Solution().shortestBeautifulSubstring(s =s , k = k))
import sys
sys.path.append("C:/Users/zrj21/Desktop/code_game/python")
import t
print(t.k)