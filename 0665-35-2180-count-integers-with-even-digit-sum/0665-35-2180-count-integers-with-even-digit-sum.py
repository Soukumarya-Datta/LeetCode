class Solution:
    def countEven(self, num: int) -> int:
        if self.isEven(num):
            return num // 2
        return (num - 1) // 2
        
    def isEven(self, num: int) -> bool:
        evenSum = True
        while num != 0:
            evenSum = not (evenSum ^ (num & 1 == 0))
            num //= 10
        return evenSum