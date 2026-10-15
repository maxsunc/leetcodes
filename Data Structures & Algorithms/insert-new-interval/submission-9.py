class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # we'll also need to merge intervals with our newInterval if they overlap

        # is overlapping intervals inclusive?

        # 2 steps:

        # 1: iterate through the intervals
        # if the endTime is less than our newInterval start time:
        # just add it ot the result 
        # overlap is inclusive

        # check if overlap
        # check 4 things: startTime of interval is less than our end time or endTime of interval is greater than our startTime
        # check the vice versa

        # merge the interval if it procs
        # the moment we dont find an overlap exit the loop


        # 2nd part: iterate through the intervals and add the rest


        res = []

        i = 0
        while i < len(intervals):
            start,end = intervals[i]
            ourStart,ourEnd = newInterval
            if end < ourStart:
                res.append(intervals[i])
                i += 1
                continue
            
            # check if there is overlap
            if ourStart <= start <= ourEnd or ourStart <= end <= ourEnd or start <= ourStart <= end or start <= ourEnd <= end:
                newInterval = [min(ourStart,start), max(ourEnd,end)]
                # print(f"overlapping {newInterval}")
            else:
                # no overlap
                break

            i += 1
        res.append(newInterval)
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res
