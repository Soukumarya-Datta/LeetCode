class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        b=Counter(s)
        c=Counter(target)
        mini=100
        for i in c:
            mini=min(mini, b[i]//c[i])
        return mini