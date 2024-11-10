class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        diff = 0
        nums.sort()
        for i in range(len(nums) - 1):
            diff = max(diff, nums[i+1] - nums[i])
        return 0 if len(nums) <= 1 else diff