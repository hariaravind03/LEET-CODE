class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        for i in range(len(matrix)):
            set1=set()
            set2=set()
            for j in range(len(matrix)):
                set1.add(matrix[i][j])
                set2.add(matrix[j][i])
            if len(set1) != n or len(set2) != n:
                return False
        return True 