class Solution:
    def fib(self, n: int) -> int:
        res = []
        res.append(0)
        res.append(1)
        for i in range(2,31):
            res.append(res[i-1] + res[i-2])
        return res[n]