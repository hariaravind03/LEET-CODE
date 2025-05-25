class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dict1={}

        for i,num in enumerate(nums):
            if num in dict1 and i-dict1[num]<=k:
                return True
            dict1[num]=i
        return False