class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        ans = 0
        if 1 in c.values(): return -1
        for i in c.values():
            ans += i//3
            if i%3==2 or i%3==1:
                ans+=1
        return ans