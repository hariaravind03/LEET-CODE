class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        l = 0
        r = n - 1
        a = []
        while l < n:
            st = s[l:r + 1]
            if st == st[::-1]:
                a.append(st)
            r -= 1
            
            if r < l:
                l += 1
                r = n - 1
        a.sort(key=len)
        return a[-1]
