class Solution:
    def splitNum(self, num: int) -> int:
        a, b = [], []
        for i, c in enumerate(sorted(str(num))):
            (a if i % 2 == 0 else b).append(c)
        return int(''.join(a)) + int(''.join(b))
        