class Solution(object):
    def reverseWords(self, s):
        b=reversed(list(s.split()))
        a=' '.join(b)
        return a
        """
        :type s: str
        :rtype: str
        """
        