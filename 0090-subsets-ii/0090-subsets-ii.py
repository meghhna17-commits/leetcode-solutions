class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        subset = []

        def bt(i):
            res.append(subset[:])

            for j in range(i, len(nums)):
                if j != i and nums[j] == nums[j - 1]:
                    continue

                subset.append(nums[j])
                bt(j + 1)
                subset.pop()

        bt(0)
        return res