class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        c = {}
        for i, n in enumerate(s):
            if n in c.keys():
                if c[n] != t[i]:
                    return False
                continue
            if t[i] in c.values():
                if n != list(c.keys())[list(c.values()).index(t[i])]:
                    return False
            c[n] = t[i]
        return True