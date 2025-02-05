class Solution:
    def lastStoneWeight(self, s: List[int]) -> int:
        while (len(s) > 1):
            s.sort()
            y = s.pop()
            x = s.pop()
            s.append(y-x)
        if len(s) == 1:
            return s[0]
        else:
            return 0