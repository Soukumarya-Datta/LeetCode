class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ind_j = []
        for ind, elem in enumerate(nums):
            if elem == key:
                ind_j.append(ind)
        res = []
        for i in range(len(nums)):
            for j in ind_j:
                if abs(i - j) <= k:
                    res.append(i)
                    break
        return sorted(res)