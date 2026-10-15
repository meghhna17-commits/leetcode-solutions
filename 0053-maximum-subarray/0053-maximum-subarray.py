class Solution(object):
    def maxSubArray(self, nums):
        sum=0
        max=nums[0]
        n=len(nums)
        for i in range(0,n):
            sum=sum+nums[i]
            if(sum>max):
                max=sum
            if sum<0:
                sum=0
        return max
        