class Solution(object):
    def countGoodNumbers(self, n):
        mod = 10**9 + 7

        if n % 2 == 0:
            a = n // 2
            b = n // 2
        else:
            a = (n // 2) + 1
            b = n // 2

        c = pow(5, a, mod)
        d = pow(4, b, mod)

        return (c * d) % mod
