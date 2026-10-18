class Solution(object):
    def findMin(self, nums):
        high=len(nums)-1
        low=0
        ans=nums[0]
        while(low<=high):
            mid= (high+low)//2
            if(nums[low]<=nums[mid]):
                ans=min(ans,nums[low])
                low=mid+1
            else:
                ans=min(ans,nums[mid])
                high=mid-1

        return ans
        