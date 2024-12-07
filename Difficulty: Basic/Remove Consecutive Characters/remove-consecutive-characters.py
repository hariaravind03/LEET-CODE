#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        d=""
        d+=s[0]
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                continue
            else:
                d+=s[i]
            
        return d
                
                
            
            
            # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

        print("~")
# } Driver Code Ends