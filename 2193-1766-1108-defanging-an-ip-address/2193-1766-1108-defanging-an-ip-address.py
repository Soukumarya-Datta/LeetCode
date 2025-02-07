class Solution:
    def defangIPaddr(self, a: str) -> str:
        return '[.]'.join(a.split('.'))