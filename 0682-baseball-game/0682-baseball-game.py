class Solution:
    def calPoints(self, op: List[str]) -> int:
        s = []
        for i in op:
            if i == 'C':
                s.pop()
            elif i == 'D':
                s.append(s[-1] << 1)
            elif i == '+':
                s.append(s[-1] + s[-2])
            else:
                s.append(int(i))
        return sum(s)