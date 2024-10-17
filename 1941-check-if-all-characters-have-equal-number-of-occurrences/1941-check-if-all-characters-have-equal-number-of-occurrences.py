class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return (len(set(list(Counter(s).values()))) == 1)