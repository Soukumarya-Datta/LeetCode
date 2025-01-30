class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, n in enumerate(words):
            if x in n:
                res.append(i)
        return res