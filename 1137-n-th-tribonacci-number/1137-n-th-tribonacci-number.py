class Solution:
    def tribonacci(self, n: int) -> int:
        res = []
        res.append(0)
        res.append(1)
        res.append(1)
        for i in range(3, 38):
            res.append(res[i-1] + res[i-2] + res[i-3])
        return res[n]