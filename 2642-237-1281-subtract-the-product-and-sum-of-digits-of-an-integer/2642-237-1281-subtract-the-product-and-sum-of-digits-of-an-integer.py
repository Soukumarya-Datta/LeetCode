class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        res = [int(i) for i in s]
        prod = 1
        for i in res:
            prod *= i
        return prod - sum(res)