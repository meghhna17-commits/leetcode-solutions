class Solution(object):
    
       
    def majorityElement(self, nums):
        n = len(nums)
        hp = {}

        for x in nums:
            if x in hp:
                hp[x] += 1
            else:
                hp[x] = 1

        ans = []

        for x in hp:
            if hp[x] > n // 3:
                ans.append(x)

        return ans
        