class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        for i, j in enumerate(num):
            if c[chr(i+48)] != int(j):
                return False
        return True