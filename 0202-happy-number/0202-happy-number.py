class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        res = set()
        
        while n != 1 and n not in res:
            res.add(n)
            n = sum_of_squares(n)
        
        return n == 1