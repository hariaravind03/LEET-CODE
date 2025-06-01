class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentlen=0
        maxlen=0
        longstring=""
        for i in range(len(s)):
            if s[i] not in longstring:
                longstring+=s[i]
                currentlen+=1
            else:
                index = longstring.index(s[i])
                longstring=longstring[index + 1:]+s[i]
                currentlen=len(longstring)
            maxlen=max(maxlen,currentlen)

        return maxlen
