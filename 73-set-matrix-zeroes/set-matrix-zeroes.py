class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        a1=[]
        a2=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    a1.append(i)
                    a2.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in a1 or j in a2:
                    matrix[i][j]=0        