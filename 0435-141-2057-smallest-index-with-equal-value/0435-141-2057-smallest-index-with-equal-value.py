class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        l=[]
        for i in range(0,len(nums)):
            if i%10==nums[i]:
                l.append(i)
                break
        if l==[]:
            return -1
        else:
            return i