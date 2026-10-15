class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        left = 1
        right = 1
        ans = nums[0]

        for i in range(n):
            if left == 0:
                left = 1

            if right == 0:
                right = 1

            left = left * nums[i]
            right = right * nums[n-i-1]

            ans = max(ans, left, right)

        return ans