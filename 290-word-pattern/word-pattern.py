class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        d1={}
        d2={}
        s=s.split(" ")
        if len(s)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in d1:
                d1[pattern[i]]=i
    
            if s[i] not in d2:
                d2[s[i]]=i
    
            if d1[pattern[i]] != d2[s[i]]:
                return False
        return True

