class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s1 = sum(nums)
        s2 = 0
        for i, n in enumerate(nums):
            s1 -= n
            if s1 == s2:
                return i
            s2 += n
        return -1