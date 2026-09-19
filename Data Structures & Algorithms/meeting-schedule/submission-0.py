"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key= lambda i : i.start)


        for idx in range(1,len(intervals)):

            interval_1 = intervals[idx - 1]
            interval_2 = intervals[idx]

            if interval_1.end > interval_2.start:
                return False
        

        return True




