class Solution(object):
    def majorityElement(self, nums):
        hp={}
        for x in nums:
            if (x in hp):
                hp[x]=hp[x]+1
            else:
                 hp[x]=1
        for x in nums:
            if(hp[x]>len(nums)/2):
                return x
        