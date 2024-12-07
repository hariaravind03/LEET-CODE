#User function Template for python3
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        l = 0
        r = n - 1
        a = []
        i = 0
        while l < n:
            st = s[l:r + 1]
            if st == st[::-1]:
                a.append(st)
                i = 1
            r -= 1
            
            if r < l:
                l += 1
                r = n - 1
        if i == 0:
            return s[0]
        
        # Sort palindromes by length, breaking ties by order of appearance
        a.sort(key=lambda x: (-len(x), s.index(x)))
        return a[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalindrome(S)

        print(ans)
# } Driver Code Ends