class Solution(object):
    def findMedianSortedArrays(self,nums1, nums2):
        c=nums1+nums2
        c.sort()
        if len(c)%2==1:
            return c[len(c)//2]
        else:
            return (float(c[len(c)//2])+float(c[(len(c)//2)-1]))/2.0
        
        