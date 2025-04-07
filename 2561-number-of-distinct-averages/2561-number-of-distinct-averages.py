class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        hashmap = {} 
        while len(nums) != 0:
            maxnum , minnum = len(nums) - 1, 0 
            if (( nums[minnum] + nums[maxnum] ) / 2) in hashmap:
                hashmap[(( nums[minnum] + nums[maxnum] ) / 2)] += 1
                nums.pop(0)
                nums.pop(-1)
            else:
                hashmap[(( nums[minnum] + nums[maxnum] ) / 2)] = 1
                nums.pop(0)
                nums.pop(-1)
        return len(hashmap)