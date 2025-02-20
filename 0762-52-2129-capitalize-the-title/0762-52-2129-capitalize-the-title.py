class Solution:
    def capitalizeTitle(self, t: str) -> str:
        s = t.split(" ")
        for i in range(len(s)):
            s[i] = s[i].lower()
            if len(s[i]) > 2:
                s[i] = s[i][0].upper() + s[i][1:]
        return ' '.join(s)