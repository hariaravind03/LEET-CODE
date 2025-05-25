class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=str(n)
        sum1=n
        set1=set()
        while sum1!=1:
            if sum1 in set1:
                return False
            set1.add(sum1)
            s=str(sum1)
            sum1=0
            for i in s:
                sum1+=int(i)*int(i)
        return True
            