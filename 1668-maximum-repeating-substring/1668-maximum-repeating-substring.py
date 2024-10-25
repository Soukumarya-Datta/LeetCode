class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        k = 1
        while word*k in sequence:
            ans += 1
            k += 1
        return ans