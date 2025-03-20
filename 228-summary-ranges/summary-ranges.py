class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        arr=[]
        if nums==[]:
            return []
        s=nums[0]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]!=1:
                if s==nums[i-1]:
                    arr.append(str(s))
                    s=nums[i]
                    continue
                arr.append(str(s)+"->"+str(nums[i-1]))
                s=nums[i]
            elif nums[i]-nums[i-1]==1 and i==(len(nums)-1):
                if s==nums[i]:
                    arr.append(str(s))
                arr.append(str(s)+"->"+str(nums[i]))
                continue
            else:
                continue
        if s==nums[-1]:
            arr.append(str(s))
        return arr