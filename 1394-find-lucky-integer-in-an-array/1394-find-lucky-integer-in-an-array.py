class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(sorted(arr, reverse=True))
        for i, j in c.items():
            if i == j:
                return i
        return -1