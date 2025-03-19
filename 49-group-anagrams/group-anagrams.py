class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        d={}
        for i in strs:
            arr=[0]*26
            for j in i:
                arr[ord(j)-ord('a')]+=1
            c=tuple(arr)

            if c not in d:
                d[c]=[]
            d[c].append(i)

        return list(d.values())