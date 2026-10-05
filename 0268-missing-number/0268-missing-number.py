class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        sum=(n*(n+1))//2
        real=0
        for i in range(0,n):
            real=real+nums[i]
        return sum-real
        