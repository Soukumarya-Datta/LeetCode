from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = 0
        for i, n in c.items():
            res += n//2
        return [res, len(nums) - (res*2)]