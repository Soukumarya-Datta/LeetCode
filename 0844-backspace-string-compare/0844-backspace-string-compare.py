class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = []
        b = []
        for char in s:
            if char == "#":
                if a:
                    a.pop()
            else:
                a.append(char)
        
        for char in t:
            if char == "#":
                if b:
                    b.pop()
            else:
                b.append(char)
        return a == b