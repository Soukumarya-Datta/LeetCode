class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums = sorted(nums)
        c = 0
        for i in range(1, len(nums) - 1):
            if(nums[0] < nums[i] and nums[len(nums) - 1] > nums[i]):
                c += 1
        return c
