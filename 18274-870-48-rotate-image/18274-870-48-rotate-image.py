class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(a)):
            for j in range(i, len(a)):
                a[i][j], a[j][i] = a[j][i], a[i][j]
        
        for i in a:
            i.reverse()