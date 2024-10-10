class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c = Counter((s1 + " " + s2).split(' '))
        res = []
        for i in c:
            if c[i] < 2:
                res.append(i)
        
        return res