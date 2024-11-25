#User function Template for python3
class Solution:

	def maxProduct(self,nums):
	    min_product = nums[0]
        max_product = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = max(num, max_product * num, min_product * num)
            min_product = min(num, max_product * num, min_product * num)
            max_product = temp_max


            result = max(result, max_product)

        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends