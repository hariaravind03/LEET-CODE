class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for j in s:
            if j.isalnum():
                res+=j.lower()


        return True if res==res[::-1] else False