class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        subset = []

        def bt(start, target):
            if len(subset) == k:
                if target == 0:
                    res.append(subset[:])
                return

            for num in range(start, 10):
                if num > target:
                    break

                subset.append(num)
                bt(num + 1, target - num)
                subset.pop()

        bt(1, n)
        return res