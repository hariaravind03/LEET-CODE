class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row=len(triangle)
        m=triangle[row-1].copy()
        for r in range(row-2, -1, -1):
            for c in range(r+1):
                m[c] = min(m[c], m[c+1]) + triangle[r][c]
        return m[0]