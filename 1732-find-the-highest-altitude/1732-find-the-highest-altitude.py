class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi, cur = 0, 0
        for i in gain:
            cur += i
            maxi = max(maxi, cur)
        return maxi
