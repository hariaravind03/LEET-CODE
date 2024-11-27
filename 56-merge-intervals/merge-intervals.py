class Solution(object):
    def merge(self,intervals):
        if not intervals:
            return []

    # Step 1: Sort intervals by the starting time
        intervals.sort(key=lambda x: x[0])

    # Step 2: Initialize the merged list
        merged = []

    # Step 3: Iterate through the sorted intervals
        for interval in intervals:
        # If merged is empty or no overlap, add the current interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # Overlapping intervals, merge them by updating the end time
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


