class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for i in range(30):
            if Counter(str(n)) == Counter(str(2**i)):
                return True
        return False
