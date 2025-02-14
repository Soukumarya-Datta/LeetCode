class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
       res = ""
       i = 0
       while (i < min(len(w1), len(w2))):
          res += w1[i] + w2[i]
          i += 1
       if len(w1) > len(w2):
          res += w1[i:]
       else:
          res += w2[i:]
       return res