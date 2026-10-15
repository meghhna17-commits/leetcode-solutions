class Solution(object):
    def merge(self, nums1, m, nums2, n):
        left=m-1
        right=0
        while(left>=0 and right<n):
            if(nums1[left]>nums2[right]):
                nums1[left],nums2[right]=nums2[right],nums1[left]
                left=left-1
                right=right+1
            else: break
        nums1[:m] = sorted(nums1[:m])
        nums2.sort()
        nums1[m:] = nums2[:n]


        