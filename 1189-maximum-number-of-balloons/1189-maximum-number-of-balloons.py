class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b=Counter(text)
        c=Counter("balloon")
        mini=10000
        for i in c:
            mini=min(mini, b[i]//c[i])
        return mini