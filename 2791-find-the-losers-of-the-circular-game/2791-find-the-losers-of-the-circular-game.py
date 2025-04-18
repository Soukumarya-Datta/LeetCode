class Solution:
    def circularGameLosers(self, n, k):
        remain, ball, nxt = set(N:=range(1,n)), k,0
        for _ in N:
            nxt = (nxt + ball)%n
            if nxt not in remain: break
            remain.remove(nxt)          
            ball+= k 
        return [i+1 for i in remain]