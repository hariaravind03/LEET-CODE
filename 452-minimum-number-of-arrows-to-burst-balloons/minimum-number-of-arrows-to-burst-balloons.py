class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:x[1])
        count=1
        end=points[0][1]
        for i in range(1,len(points)):
            if points[i][0]>end:
                count+=1
                end=points[i][1]

        return count