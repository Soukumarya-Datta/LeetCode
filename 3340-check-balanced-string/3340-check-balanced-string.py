class Solution:
    def isBalanced(self, num: str) -> bool:
        eve = 0
        odd = 0
        for i, n in enumerate(num):
            if i % 2 == 0:
                eve += ord(n) - 48
            else:
                odd += ord(n) - 48
        return eve == odd