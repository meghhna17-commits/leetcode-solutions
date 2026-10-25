
class Solution(object):
    def maxDepth(self, s):
        count = 0
        maxi = 0

        for i in s:
            if i == '(':
                count += 1
                maxi = max(maxi, count)

            elif i == ')':
                count -= 1

        return maxi
