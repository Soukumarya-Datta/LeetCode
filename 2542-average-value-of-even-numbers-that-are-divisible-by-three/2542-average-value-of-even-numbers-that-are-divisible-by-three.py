import math

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        len_nums = len(nums)
        
        sum_even_nums_divisible_by_three = 0
        count_even_nums_divisible_by_three = 0
        i = 0
        while (i < len_nums):
            num = nums[i]
            if (num % 6 == 0):
                sum_even_nums_divisible_by_three += nums[i]
                count_even_nums_divisible_by_three += 1
            i += 1

        return math.floor(sum_even_nums_divisible_by_three / max(1, count_even_nums_divisible_by_three))