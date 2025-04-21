class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n) + str(2*n) + str(3*n)
        if len(set(s)) == 9 and len(s) == 9 and '0' not in s:
            return True
        return False