class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        for i in c.values():
            if i == max(c.values()):
                res += i
        return res