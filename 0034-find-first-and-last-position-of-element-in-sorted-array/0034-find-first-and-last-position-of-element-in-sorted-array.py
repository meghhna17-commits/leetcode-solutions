
class Solution(object):
    def searchRange(self, nums, target):
        first = self.firstOccurrence(nums, target)
        last = self.lastOccurrence(nums, target)
        return [first, last]

    def firstOccurrence(self, nums, target):
        low = 0
        high = len(nums) - 1
        first = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return first

    def lastOccurrence(self, nums, target):
        low = 0
        high = len(nums) - 1
        last = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return last

        