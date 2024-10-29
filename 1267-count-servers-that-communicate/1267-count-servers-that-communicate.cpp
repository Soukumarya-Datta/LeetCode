class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        int M = grid.size(), N = grid[0].size(), res = 0;
        vector<int> colCnt(M, 0), rowCnt(N, 0);
        for (int i = 0; i < M; i++) 
            for (int j = 0; j < N; j++) 
                if (grid[i][j]) 
                {
                    colCnt[i]++;
                    rowCnt[j]++;
                }
        for (int i = 0; i < M; i++) 
            for (int j = 0; j < N; j++) 
                if (grid[i][j] && (colCnt[i] > 1 || rowCnt[j] > 1)) 
                    res++;
        return res;
    }
};