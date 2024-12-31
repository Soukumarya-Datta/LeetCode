from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for i, n in c.items():
            if(n % 2 != 0):
                return False
        return True