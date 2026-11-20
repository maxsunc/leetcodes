class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # curInterval
        # sort intervals by start

        # if end overlaps with thier start, curInterval[1] >= interval[0]
        # merge into curInterval
        # if no overlap, append and replace cur Interval
        if len(intervals) == 0:
            return
        intervals.sort(key = lambda x: x[0])
        curInterval = list(intervals[0])
        res = []

        for i in range(0, len(intervals)):
            interval = intervals[i]
            if curInterval[1] >= interval[0]:
                # merge it
                curInterval = [min(interval[0], curInterval[0]), max(curInterval[1],interval[1])]
            else:
                # no overlap, append and replace
                res.append(curInterval.copy())
                curInterval = interval
        res.append(curInterval.copy())
        return res


