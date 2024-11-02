class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        c = Counter()
        for i, n in enumerate(senders):
            c[n] += len(messages[i].split(' '))
        return max(c.keys(), key=lambda x: (c[x], x))