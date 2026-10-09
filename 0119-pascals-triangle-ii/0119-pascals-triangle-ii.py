class Solution(object):
    def getRow(self, rowIndex):
        ans = [1]
        res = 1

        for i in range(1, rowIndex + 1):
            res = res * (rowIndex - i + 1) // i
            ans.append(res)

        return ans