class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=1
        m=nums[0]

        for i in range(len(nums)):
            if m!=nums[i]:
                c-=1
                if c==0:
                    m=nums[i]
                    c+=1
            else:
                c+=1
        return m
