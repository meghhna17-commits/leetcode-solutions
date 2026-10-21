
class Solution(object):
    def minDays(self, bloomDay, m, k):
        n = len(bloomDay)

        if m * k > n:
            return -1

        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            bouquets = 0
            flowers = 0

            for i in range(n):
                if bloomDay[i] <= mid:
                    flowers += 1
                else:
                    flowers = 0

                if flowers == k:
                    bouquets += 1
                    flowers = 0

            if bouquets >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
