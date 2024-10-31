class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        tmp = sorted(nums, reverse = True)
        if tmp[1] <= tmp[0] // 2:
            return nums.index(tmp[0])
        return -1