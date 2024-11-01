class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        c = 0
        sum = 0
        for i in nums:
            sum += i
            if sum == 0:
                c += 1
        return c