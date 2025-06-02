class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1=0

        for i in range(len(mat)):
            sum1+=mat[i][i]
            sum1+=mat[i][len(mat)-1-i]
        if len(mat)%2==0:
            return sum1
        else:
            return sum1-mat[len(mat)//2][len(mat)//2]