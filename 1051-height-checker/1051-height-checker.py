class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        tmp = sorted(heights)
        c = 0
        for i in range(len(heights)):
            if tmp[i] != heights[i]:
                c += 1
        return c