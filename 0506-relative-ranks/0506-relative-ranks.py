class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res=[]
        tmp=score.copy()
        score.sort()
        score.reverse()
        dict_score=dict()
        for i in range(0,len(score),1):
            dict_score[score[i]]=str(i+1)
        for value in tmp:
            res.append(dict_score[value])
        for i in range(len(res)):
            if res[i]=='1':
                res[i]="Gold Medal"
            elif res[i]=='2':
                res[i]="Silver Medal"
            elif res[i]=='3':
                res[i]='Bronze Medal'
        return res