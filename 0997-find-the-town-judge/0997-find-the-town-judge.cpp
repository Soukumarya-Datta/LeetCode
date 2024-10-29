class Solution {
public:
       int findJudge(int N, vector<vector<int>>& trust) 
    {
        int knows[N+1];
        int known[N+1];
        memset(knows,0,sizeof(knows));
        memset(known,0,sizeof(known));
        for(int i = 0; i<trust.size(); i++)
        {
            int a = trust[i][0],b = trust[i][1];
            knows[a]++;
            known[b]++;
        }
        for(int i = 1; i<=N; i++)
        if(knows[i] == 0 && known[i] == N-1)
            return i;
        return -1;
    }
};