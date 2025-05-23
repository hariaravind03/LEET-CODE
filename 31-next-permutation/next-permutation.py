class Solution(object):
    def nextPermutation(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i=len(arr)-2

        while i>=0 and arr[i]>=arr[i+1]:
            i-=1

        if i>=0:
            j=len(arr)-1

            while arr[j]<=arr[i]:
                j-=1

            arr[i],arr[j]=arr[j],arr[i]

        arr[i+1:]=reversed(arr[i+1:])