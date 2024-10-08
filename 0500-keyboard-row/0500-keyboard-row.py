class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = set("qwertyuiop")
        b = set("asdfghjkl")
        c = set("zxcvbnm")
        result = []
        
        for word in words:
            lrw = word.lower()
            
            if (set(lrw) <= a) or (set(lrw) <= b) or (set(lrw) <= c):
                # a <= b means if a subset of b
                result.append(word)

        return result