class Solution(object):
    def subarraySum(self, nums, k):
        mp = {0: 1}
        prefixSum = 0
        count = 0

        for i in range(len(nums)):
            prefixSum += nums[i]

            rem = prefixSum - k

            if rem in mp:
                count += mp[rem]

            if prefixSum in mp:
                mp[prefixSum] += 1
            else:
                mp[prefixSum] = 1

        return count