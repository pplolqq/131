class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=s[0]
        sw={}
        for i,x in enumerate(s):
            if x in sw:
                for j in sw[x]: 
                    ts=s[j:i+1]
                    if ts==ts[::-1] and len(ts)>len(res):
                        res=ts
    
                sw[x].append(i)
            else:sw[x]=[i]
        print(sw["a"])
        print(res)
# Solution().longestPalindrome("babadada")
class Solution:
    def minIncrementOperations(self, nums: list[int], k: int) -> int:
        n=len(nums)
        F=[[-1]*n]*3
        def f(i,j):
            if i<0:
                return 0
            # print(i,j,F[j][i])
            if F[j][i] !=-1:
                return F[j][i]
            res=f(i-1,0)+max(k-nums[i],0)
            if j<2:
                res=min(f(i-1,j+1),res)
            # F[j][i]=res
            F[j][i]=res
            print(i,j,res,F[j][i])
            return res
        return f(n-1,0)


Solution().minIncrementOperations([2,2,3,43],4)
# F=[[-1]*4]*3
print([[-1,-1] for i in range(2)])
