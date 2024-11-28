class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a={}
        b=[]
        for i in range(len(nums)):
            if nums[i] not in a:
                a[nums[i]]=1
            else:
                a[nums[i]]+=1
        
        for i in a:
            if a[i]>len(nums)/3:
                b.append(i)
        return b