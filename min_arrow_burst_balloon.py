class Solution:
    def overlap(self, a, b):
        #return true if interval a and b overlap
        p,q = a
        r,s = b    
        return (r >= p and r <= q) or (s >= p and s <= q) or (p >= r and p <= s) or (q >= r and q <= s)

    def interval(self, a, b):
        #return the overlap interval between a and b if they overlap
        p,q = a
        r,s = b
        return [max(p,r), min(q,s)]

    def findMinArrowShots(self, points: List[List[int]]) -> int:    
        #sort
        points = sorted(points, key=lambda x: x [0])
        #arrow list
        arrow = [points[0]]

        for i in range(len(points)):
            if self.overlap(arrow[-1], points[i]):
                arrow[-1] = self.interval(arrow[-1], points[i])
            else: 
                arrow.append(points[i])

        return len(arrow)
