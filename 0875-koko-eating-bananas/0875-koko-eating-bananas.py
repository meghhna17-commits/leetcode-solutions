class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            total = 0

            for i in range(len(piles)):
                total += piles[i] // mid + (1 if piles[i] % mid != 0 else 0)

            if total <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans