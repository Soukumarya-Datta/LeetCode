class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        original_sum = len(nums) * (len(nums) + 1) // 2 #10
        lst_sum = sum(nums)                             #9
        tmp_set = set(nums)
        set_sum = sum(tmp_set)                          #7

        res.append(abs(lst_sum - set_sum))
        res.append(abs(set_sum - original_sum))
        return res