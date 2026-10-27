
class Solution(object):
    def myPow(self, x, n):
        nn = n
        if nn < 0:
            nn = -1 * nn

        ans = 1.0

        while nn:
            if nn % 2 == 1:
                ans = ans * x
                nn = nn - 1
            else:
                x = x * x
                nn = nn // 2

        if n < 0:
            ans = 1.0 / ans

        return ans
