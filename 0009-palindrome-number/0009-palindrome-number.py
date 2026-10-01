class Solution(object):
    def isPalindrome(self, x):
        abs1=abs(x)
        yes=int(str(abs1)[::-1])
        if (x>=0 and yes==abs1):
            return True
        else:
            return False

        
        