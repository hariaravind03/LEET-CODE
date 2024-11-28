class Solution(object):
    def largestOddNumber(self, nums):
        """
        :type num: str
        :rtype: str
        """
        for i in range(len(nums)-1,-1,-1):
            if int(nums[i])%2!=0:
                return nums[:i+1]
        return ""

        
        
        