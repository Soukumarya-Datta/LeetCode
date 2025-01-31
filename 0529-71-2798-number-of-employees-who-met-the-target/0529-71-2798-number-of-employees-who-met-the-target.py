class Solution:
    def numberOfEmployeesWhoMetTarget(self, h: List[int], t: int) -> int:
        c = 0
        for i in h:
            if i >= t:
                c += 1
        return c