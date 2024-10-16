class Solution:
    def repeatedCharacter(self, s: str) -> str:
        stack = []
        for c in s:
            if c in stack:
                return c
            stack.append(c)