class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if not i or nums[i-1] >= nums[i]:
                sum = 0
            sum += nums[i]
            res = max(res,sum)
        return res

        

