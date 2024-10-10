from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])

        for i in words[1:]:
            count &= Counter(i)

        return list(count.elements())