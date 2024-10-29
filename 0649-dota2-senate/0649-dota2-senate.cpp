class Solution {
public:
    string predictPartyVictory(string s) {
        queue<int> q;
        int peo[2]={0},ban[2]={0};
        for(int i=0;i<s.length();i++)
        {
            int x=(s[i]=='R')?1:0;
            peo[x]++;
            q.push(x);
        }
        while(peo[0]>0 && peo[1]>0)
        {
            int x=q.front();
            q.pop();
            if(ban[x]>0)
            {
                ban[x]--;
                peo[x]--;
            }
            else
            {
                ban[x^1]++;
                q.push(x);
            }
        }
        return peo[1]>0?"Radiant":"Dire";
    }
};