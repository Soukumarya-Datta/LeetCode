class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int: 
        res = []
        for i in sentences:
            ls = i.split()
            res.append(len(ls))
        return max(res)