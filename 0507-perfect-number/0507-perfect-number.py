import math

class Solution(object):

    def checkPerfectNumber(self, num):

        if num <= 1:
            return False

        total = 1

        for i in range(2, int(math.sqrt(num)) + 1):

            if num % i == 0:
                total += i
                total += num // i

        return total == num