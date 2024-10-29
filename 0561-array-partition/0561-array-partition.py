class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for i in nums[::2]:
            sum += min(i,i+1)
        return sum