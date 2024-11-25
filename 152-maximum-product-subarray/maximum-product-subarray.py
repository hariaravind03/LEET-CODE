class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product=nums[0]
        min_product=nums[0]
        result=nums[0]


        for i in range(1,len(nums)):
            num=nums[i]

            temp_max=max(num,max_product*num,min_product*num)
            min_product=min(num,max_product*num,min_product*num)
            max_product=temp_max

            result=max(result,max_product)

        return result
        