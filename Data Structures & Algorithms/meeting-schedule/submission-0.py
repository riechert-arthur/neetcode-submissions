"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda s: s.start)
        
        for i in range(len(intervals) - 1):
            interval = intervals[i]
            duration = interval.end - interval.start
            if interval.start + duration > intervals[i + 1].start:
                return False

        return True