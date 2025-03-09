class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        count = Counter(nums)
        while count[original]:
            original <<= 1
        return original