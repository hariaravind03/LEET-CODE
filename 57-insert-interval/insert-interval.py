class Solution(object):
    def insert(self, intervals, newInterval):

        if not intervals and not newInterval:
            return []
        if not intervals:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort()

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged