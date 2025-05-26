class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict1={}
        dict2={}
        for i in ransomNote:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for i in magazine:
            if i not in dict2:
                dict2[i]=1
            else:
                dict2[i]+=1
        
        for i in dict1:
            if i not in dict2:
                return False
            if dict1[i]<=dict2[i]:
                continue
            else:
                return False
        return True
