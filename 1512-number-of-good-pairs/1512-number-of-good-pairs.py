class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = Counter(nums)
        c = 0
        for i in res:
            c += res[i]*(res[i]-1) // 2
        return c