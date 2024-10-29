class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = [x for x in nums if x != 0]
        if nums: return len(set(nums))
        else: return 0