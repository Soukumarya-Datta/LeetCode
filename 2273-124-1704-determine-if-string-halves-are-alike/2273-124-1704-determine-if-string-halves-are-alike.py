class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a = 0
        b = 0
        for i in s[:len(s) // 2]:
            if i in vow:
                a += 1

        for i in s[len(s) // 2:]:
            if i in vow:
                b += 1
        return a == b