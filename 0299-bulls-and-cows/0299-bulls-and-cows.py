class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=0
        cows=0
        secretd={}
        guessd={}
        for i ,j in zip(secret,guess):
            if i==j:
                bulls+=1
            else:
                secretd[i]=secretd.get(i,0)+1
                guessd[j]=guessd.get(j,0)+1
        for i in secretd:
            if i in guessd:
                cows+=min(secretd[i],guessd[i])
        return f"{bulls}A{cows}B"