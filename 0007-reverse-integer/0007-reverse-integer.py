class Solution(object):

    def reverse(self, x):

        sign = -1 if x < 0 else 1
        x = abs(x)

        reverse = 0

        while x > 0:

            last = x % 10
            x = x // 10

            if reverse > (2**31 - 1 - last) // 10:
                return 0

            reverse = (reverse * 10) + last

        return sign * reverse
        