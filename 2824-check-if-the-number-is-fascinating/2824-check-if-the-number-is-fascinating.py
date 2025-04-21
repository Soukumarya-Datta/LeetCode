from collections import Counter
class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n) + str(2 * n) + str(3 * n)
        c = Counter()
        for i in s:
            if c[i] == 0:
                c[i] = 1
            else:
                return False
        print(len(c))
        if(len(c) == 9 and '0' not in c.keys()):
            return True
        return False