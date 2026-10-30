class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        subset = []
        candidates.sort()

        def bt(i, target):
            if target == 0:
                res.append(subset[:])
                return

            if i == len(candidates):
                return

            
            if candidates[i] <= target:
                subset.append(candidates[i])
                bt(i+1, target-candidates[i])
                subset.pop()

            
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            
            bt(i+1, target)

        bt(0, target)
        return res