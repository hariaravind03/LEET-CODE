class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=s.split(' ')
        res=""
        for i in string:
            for j in i:
                if j.isalnum():
                    res+=j.lower()


        return True if res==res[::-1] else False