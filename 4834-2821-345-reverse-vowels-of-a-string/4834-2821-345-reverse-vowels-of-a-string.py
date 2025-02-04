class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a', 'e', 'i', 'o', 'u']
        v = v + [x.upper() for x in v]
        t = [x for x in s if x in v]
        res = []
        
        for ch in s:
            if ch in v:
                res.append(t.pop())
            else:
                res.append(ch)
        
        return "".join(res)