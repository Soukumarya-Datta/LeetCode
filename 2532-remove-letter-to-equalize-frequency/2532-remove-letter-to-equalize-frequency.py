class Solution:
    def equalFrequency(self, word: str) -> bool:
        count={}
        for i in set(word):
            count[i]=word.count(i)
        for i in list(count.keys()):
            count[i]-=1
            if count[i]==0: del count[i]
            if len(set(count.values()))==1: return True
            if i in count: count[i]+=1
            else: count[i]=1
        return False