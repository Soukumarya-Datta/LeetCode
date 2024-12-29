class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c = 0
        for i in nums:
            if(nums.count(i-k) >= 0):
                c += nums.count(i-k)
        return c