class Solution(object):
    def removeDuplicates(self, nums):
        k=0
        s=nums[0]
        c=1
        for i in range(0,len(nums)):
            if s==nums[i] and c<=2:
                c+=1
                nums[k]=nums[i]
                k+=1
            elif s!=nums[i]:
                nums[k]=nums[i]
                k+=1
                c=2
                s=nums[i]
            else:
                continue
        return k

            