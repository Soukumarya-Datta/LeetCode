class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        cnt = bin(n).count('1')
        return cnt == 1