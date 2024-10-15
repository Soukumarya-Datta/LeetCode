class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        c = {}
        if len(pattern) != len(s.split(' ')):
            return False

        for i, n in enumerate(pattern):
            if n in c.keys():
                if c[n] != s.split(' ')[i]:
                    return False
                continue
            if s.split(' ')[i] in c.values():
                if n != list(c.keys())[list(c.values()).index(s.split(' ')[i])]:
                    return False
            c[n] = s.split(' ')[i]
        return True