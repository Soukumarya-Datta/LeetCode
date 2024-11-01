class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        after = sum(nums)
        prev = 0
        for i , num in enumerate(nums):
            after -= num
            if prev == after:
                return i
            prev += num

        return -1