class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = defaultdict(int)
        c = 0

        for i in time:
            r = i % 60
            tmp = (60 - r) % 60
            c += count[tmp]
            count[r] += 1

        return c
