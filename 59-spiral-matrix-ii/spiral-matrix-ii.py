class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        top,bottom=0,n-1
        left,right=0,n-1
        count=1
        a=[]
        for i in range(n):
            a.append([])
            for j in range(n):
                a[i].append(0)

        while top<=bottom and left<=right and count<=n*n:
            for i in range(left,right+1):
                a[top][i]=count
                count+=1
            top+=1

            for i in range(top,bottom+1):
                a[i][right]=count
                count+=1
            right-=1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    a[bottom][i]=count
                    count+=1
                bottom-=1

            if left<=right:
                for i in range(bottom,top-1,-1):
                    a[i][left]=count
                    count+=1
                left+=1
        return a

