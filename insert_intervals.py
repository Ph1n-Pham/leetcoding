"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
"""

class Solution:
    def overlap(self, a, b):
        p,q = a
        r,s = b    
        return (r >= p and r <= q) or (s >= p and s <= q) or (p >= r and p <= s) or (q >= r and q <= s)

    def merge(self, a, b):
        p,q = a
        r,s = b
        return (min(p,r), max(q,s))

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #edge cases
        if not intervals: 
            return [newInterval]
        
        if intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]
        if intervals[0][0] > newInterval[1]:
            return [newInterval] + intervals
        
        #slice index
        sindex = 0
        
        for i in range(len(intervals)):
            s,e = intervals[i]
            if e < newInterval[0]:
                continue
            if self.overlap(newInterval, (s,e)):
                intervals[i] = self.merge(newInterval, (s,e))
                sindex = i
                break
            elif e > newInterval[0]:
                intervals.insert(i, newInterval)
                sindex = i
                break
        ans = intervals[:sindex]
        for i in range(sindex, len(intervals)):
            s,e = intervals[i]
            if ans and self.overlap(ans[-1], (s,e)):
                ans[-1] = self.merge(ans[-1], (s,e))
            else: 
                ans.append((s,e))
        return ans


