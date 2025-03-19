class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr=s.split(' ')
        a=[]
        for i in arr:
            if i!="":
                a.append(i)
        return len(a[-1])