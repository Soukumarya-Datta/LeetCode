class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a = Counter(words1)
        b = Counter(words2)
        c = 0
        for i in a:
            if i in b.keys() and a[i] == b[i] and a[i] == 1:
                c += 1
        return c