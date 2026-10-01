class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        left = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                max_len = max(max_len, right - left)
                left = right + 1

        # Check the last segment
        max_len = max(max_len, len(nums) - left)

        return max_len
        