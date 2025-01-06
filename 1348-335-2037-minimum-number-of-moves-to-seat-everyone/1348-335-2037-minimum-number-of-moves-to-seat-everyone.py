class Solution:
    def minMovesToSeat(self, s: List[int], st: List[int]) -> int:
        res = 0
        s = sorted(s)
        st = sorted(st)
        for i in range(len(st)):
            res += abs(st[i] - s[i])
        return res