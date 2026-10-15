
class Solution(object):
    def reversePairs(self, nums):

        def countPairs(low, mid, high):
            count = 0
            j = mid + 1

            for i in range(low, mid + 1):
                while j <= high and nums[i] > 2 * nums[j]:
                    j += 1

                count += j - (mid + 1)

            return count

        def merge(low, mid, high):
            temp = []
            left = low
            right = mid + 1

            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1

            while left <= mid:
                temp.append(nums[left])
                left += 1

            while right <= high:
                temp.append(nums[right])
                right += 1

            nums[low:high + 1] = temp

        def mergeSort(low, high):
            if low >= high:
                return 0

            mid = (low + high) // 2

            count = mergeSort(low, mid)
            count += mergeSort(mid + 1, high)
            count += countPairs(low, mid, high)

            merge(low, mid, high)

            return count

        return mergeSort(0, len(nums) - 1)