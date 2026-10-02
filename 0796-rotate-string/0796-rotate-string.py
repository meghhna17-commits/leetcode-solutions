class Solution(object):
    def rotateString(self, s, goal):
        n = len(s)

        if len(s) != len(goal):
            return False

        for k in range(n):
            new = s[k:] + s[:k]

            if new == goal:
                return True

        return False