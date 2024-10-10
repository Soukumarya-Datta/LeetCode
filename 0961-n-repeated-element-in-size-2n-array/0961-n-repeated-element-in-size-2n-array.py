class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        #return mode(nums)

        uniq = set()
        for a in nums:
            if a not in uniq:
                uniq.add(a)
            else:
                return a