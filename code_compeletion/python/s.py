class Solution:
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
# Solution().minimumSum([8,6,1,5,3])
# import t
# print()
# import bisect
# bisect.bisect_left()
for i in range(19,0,-1):
    print(i)