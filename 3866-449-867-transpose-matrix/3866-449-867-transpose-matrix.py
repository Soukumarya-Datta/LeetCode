class Solution:
    def transpose(self, a: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(a) for _ in range(len(a[0]))]
    
        for i in range(len(a)):
            for j in range(len(a[0])):
                res[j][i] = a[i][j]
        
        return res