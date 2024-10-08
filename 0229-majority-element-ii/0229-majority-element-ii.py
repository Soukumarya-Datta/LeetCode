from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x = len(nums)//3
        ans = []
        mp = Counter(nums)
        for it in mp:
            if mp[it] > x:
                ans.append(it)
        
        return ans
        