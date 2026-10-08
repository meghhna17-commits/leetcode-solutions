class Solution(object):
    def rearrangeArray(self, nums):
        
        n=len(nums)
        ans=[0]*n
        postive=0
        negative=1
        for i in range(0,n):
            if (nums[i]>0 ):
                ans[postive]=nums[i]
                postive+=2
            else:
                ans[negative]=nums[i]
                negative+=2
        return ans