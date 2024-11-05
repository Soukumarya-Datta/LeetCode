class Solution:
    def checkString(self, s: str) -> bool:
        b = False
        for i in s:
            if i == 'b':
                b = True
            if i == 'a' and b:
                return False
        return True