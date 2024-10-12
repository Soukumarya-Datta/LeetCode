class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        A = set(nums1)
        B = set(nums2)
        res = []

        for i in A:
            if i in B:
                res.append(i)
        return res