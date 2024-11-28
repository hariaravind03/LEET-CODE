#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,s1,s2):
        d1={}
        d2={}
        
        for i in range(len(s1)):
            if s1[i] not in d1:
                d1[s1[i]]=i
            
            if s2[i] not in d2:
                d2[s2[i]]=i
            
            if d1[s1[i]]!=d2[s2[i]]:
                return False
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        p = str(input())
        ob = Solution()
        if (ob.areIsomorphic(s, p)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends