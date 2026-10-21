
class Solution(object):
    def findKthPositive(self, arr, k):
        for i in arr:
            if i <= k:
                k += 1
            else:
                break

        return k
