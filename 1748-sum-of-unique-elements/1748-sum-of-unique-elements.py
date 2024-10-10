class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = set()
        duplicates = set()

        for i in nums:
            if i in unique:
                unique.remove(i)         # 
                duplicates.add(i)        # 2
            elif i not in duplicates:
                unique.add(i)            # 1 3

        return sum(unique)