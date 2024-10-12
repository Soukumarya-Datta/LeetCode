from collections import Counter 

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        a = re.split(r'\W+', paragraph.lower())
        b = [w for w in a if w and w not in banned]

        return max(b, key = b.count)