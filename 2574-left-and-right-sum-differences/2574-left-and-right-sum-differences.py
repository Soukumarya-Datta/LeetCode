class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        s1=sum(nums)
        s2=0
        for i in range(len(nums)):
            s1-=nums[i]
            a=nums[i]
            nums[i]=abs(s2-s1)
            s2+=a
        return nums