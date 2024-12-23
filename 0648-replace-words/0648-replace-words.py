class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        words = sentence.split()
        result = []

        for word in words:
            for i in range(len(word) + 1):
                prefix = word[:i]
                if prefix in dict:
                    result.append(prefix)
                    break
            else:
                result.append(word)

        return ' '.join(result)