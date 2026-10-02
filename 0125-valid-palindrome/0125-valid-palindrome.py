class Solution(object):

    def isPalindrome(self, s):

        s = s.lower()

        new = ""

        for char in s:
            if char.isalnum():
                new += char

        return new == new[::-1]