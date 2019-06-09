class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)


def merge_intervals(intervals, new_interval):

    abc = len(intervals)
    intervals.append(new_interval)
    if abc == 0:
        return intervals
    intervals.sort(key=lambda x: x.start)
    merged = []
    for interval in intervals:
        if not merged or merged[-1].end < interval.start:
            merged.append(interval)
        else:
            merged[-1].end = max(merged[-1].end, interval.end)
    return merged
    
#A = [ (6037774, 6198243), (6726550, 7004541), (8842554, 10866536), (11027721, 11341296), (11972532, 14746848), (16374805, 16706396), (17557262, 20518214), (22139780, 22379559), (27212352, 28404611), (28921768, 29621583), (29823256, 32060921), (33950165, 36418956), (37225039, 37785557), (40087908, 41184444), (41922814, 45297414), (48142402, 48244133), (48622983, 50443163), (50898369, 55612831), (57030757, 58120901), (59772759, 59943999), (61141939, 64859907), (65277782, 65296274), (67497842, 68386607), (70414085, 73339545), (73896106, 75605861), (79672668, 84539434), (84821550, 86558001), (91116470, 92198054), (96147808, 98979097) ]
#B = (36210193, 61984219)

A = [(1,2),(3,5),(6, 7),(8, 10), (12, 16)]
B = (4, 9)
#A = [ (1, 2), (3, 6) ]
#B = (10, 8)
A = [[1,3],[6,9]]
B = [2,5]
import pdb
pdb.set_trace()
#A = []
#B = [1,1]
print('merged intervals are:-', merge_intervals(A, B))

'''
# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        
        abc = len(intervals)
        intervals.append(new_interval)
        if abc == 0:
            return intervals
        intervals.sort(key=lambda x: x.start)
        merged = []
        for interval in intervals:
            if len(merged) == 0:
                merged.append(interval)
            else:
                if merged[-1].end >interval.start:
                    val = merged[-1].start
                    merged.pop()
                    merged.append((val,interval.end))
                else:
                    merged.append(interval)
        return merged
'''
