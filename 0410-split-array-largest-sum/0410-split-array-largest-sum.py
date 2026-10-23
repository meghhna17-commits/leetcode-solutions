
class Solution(object):
    def splitArray(self, nums, k):
        if len(nums) < k:
            return -1

        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (high + low) // 2
            c = 1
            p = 0

            for i in range(len(nums)):
                if nums[i] + p <= mid:
                    p = p + nums[i]
                else:
                    c = c + 1
                    p = nums[i]

            if c <= k:
                high = mid - 1
            else:
                low = mid + 1

        return low
