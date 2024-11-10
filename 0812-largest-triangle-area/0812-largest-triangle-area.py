class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def calc(point1, point2, point3):
            x1, y1 = point1
            x2, y2 = point2
            x3, y3 = point3
            return abs(1/2 * (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)))
        
        n = len(points)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    res = max(res, calc(points[i], points[j], points[k]))
        return res