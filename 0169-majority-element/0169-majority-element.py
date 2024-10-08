from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        ans = max(c, key = c.get)
        return ans
        