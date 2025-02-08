class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split(" ")
        t = [i[::-1] for i in t]
        return " ".join(t)