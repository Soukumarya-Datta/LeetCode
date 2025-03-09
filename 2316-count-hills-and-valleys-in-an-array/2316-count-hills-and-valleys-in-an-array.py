class Solution:
    def countHillValley(self, nums):
        len_nums = len(nums)
        ret_val = 0
        i = len_nums - 2
        while (i >= 1):
            right_index = i + 1
            while (i >= 2 and nums[i] == nums[i-1]):
                i -= 1
            
            left_index = i - 1
            if nums[left_index] < nums[i] and nums[i] > nums[right_index]:
                ret_val += 1
            elif nums[left_index] > nums[i] and nums[i] < nums[right_index]:
                ret_val += 1
            i -= 1
        
        return ret_val