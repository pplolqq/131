"""
2919. 使数组变美的最小增量运算数
提示
中等
29
相关企业
给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和一个整数 k 。

你可以执行下述 递增 运算 任意 次（可以是 0 次）：

从范围 [0, n - 1] 中选择一个下标 i ，并将 nums[i] 的值加 1 。
如果数组中任何长度 大于或等于 3 的子数组，其 最大 元素都大于或等于 k ，则认为数组是一个 美丽数组 。

以整数形式返回使数组变为 美丽数组 需要执行的 最小 递增运算数。

子数组是数组中的一个连续 非空 元素序列。
 
"""
#two prama ,one for recording the position ,the other for changing states
#max , recursion , and a list for regarding the used state 
class Solution:
    def minIncrementOperations(self, nums: list[int], k: int) -> int:
        n=len(nums)
        F=[[-1,-1,-1] for _ in range(n)]
        def f(i,j):
            if i<0:
                return 0
            if F[i][j] !=-1:
                return F[i][j]
            res=f(i-1,0)+max(k-nums[i],0)
            if j<2:
                res=min(f(i-1,j+1),res)
            F[i][j]=res
            return res
        return f(n-1,0)

#func2 recurrence
    def min2(self,nums:list,k):
        pass