 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self, arr):
    # Removing duplicates and sorting
        arr = sorted(set(arr))
    
        max_len = 1
        current_len = 1

    # Iterate through the sorted array
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == 1:
            # If the current element is consecutive
                current_len += 1
            else:
            # If not consecutive, update max_len and reset current_len
                max_len = max(max_len, current_len)
                current_len = 1

        max_len = max(max_len, current_len)
    
        return max_len



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a))
        print("~")
# } Driver Code Ends