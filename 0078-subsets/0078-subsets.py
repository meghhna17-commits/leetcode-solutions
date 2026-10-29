class Solution(object):
    def subsets(self, nums):
        res=[]
        subset=[]
        def bt(i):
            if i==len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            bt(i+1)
            subset.pop()
            bt(i+1)
        bt(0)
        return res
            
        