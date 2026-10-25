
class Solution(object):
    def removeOuterParentheses(self, s):
        ans = ""
        count = 0

        for i in s:
            if i == '(':
                if count > 0:
                    ans += i
                count += 1

            else:
                count -= 1
                if count > 0:
                    ans += i

        return ans
