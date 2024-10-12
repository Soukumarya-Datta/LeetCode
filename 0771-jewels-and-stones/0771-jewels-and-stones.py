from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = Counter(stones)
        res = 0
        for i, j in c.items():
            if i in jewels:
                res += j

        return res