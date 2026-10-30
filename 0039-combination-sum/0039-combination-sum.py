class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        subset = []

        def bt(i, target):
            if i == len(candidates):
                if target == 0:
                    res.append(subset[:])
                return

            
            if candidates[i] <= target:
                subset.append(candidates[i])
                bt(i, target - candidates[i])
                subset.pop()

            
            bt(i+1, target)

        bt(0, target)
        return res