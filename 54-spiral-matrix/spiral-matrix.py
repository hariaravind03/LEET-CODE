class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        top,bottom=0,len(matrix)-1
        left,right=0,len(matrix[0])-1
        a=[]

        while top<=bottom and left<=right:

            for i in range(left,right+1):
                a.append(matrix[top][i])
            top+=1

            for i in range(top,bottom+1):
                a.append(matrix[i][right])
            right-=1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    a.append(matrix[bottom][i])
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    a.append(matrix[i][left])
                left+=1
            
        return a
