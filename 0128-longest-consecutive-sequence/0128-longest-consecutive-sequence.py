class Solution(object):
    def longestConsecutive(self, nums):
        st=set(nums)
        largest=0
        for x in st:
            if (x-1 not in st):
                count=1
                while (x+count in st):
                    count=count+1
                largest=max(count,largest)
        return largest         
                
        