#  Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetingExample1
#
# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: false

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False

        return True