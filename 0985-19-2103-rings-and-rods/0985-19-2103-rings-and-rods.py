class Solution:
    def countPoints(self, r: str) -> int:
        ans = 0
        bar = ["","","","","","","","","",""]
        for i in range(1,len(r),2) :
            bar[int(r[i])] += r[i-1]
        for b in bar:
            if "B"in b and "G" in b and "R" in b:
                ans += 1
        return ans