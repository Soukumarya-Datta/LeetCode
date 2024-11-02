class Solution:
    def frequencySort(self, s: str) -> str:
        res = ""
        c = Counter(s)
        for i in sorted(c, key = c.get, reverse = True):
            res += i * c[i]
        return res