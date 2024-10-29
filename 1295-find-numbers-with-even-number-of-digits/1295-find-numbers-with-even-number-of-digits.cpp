class Solution {
public:
    int findNumbers(vector<int>& n) {
        int c=0;
        for(int i=0;i<n.size();i++)
        {
            int eve=floor(log10(n[i]))+1;
            if(eve%2==0)
                c++;
        }
        return c;
    }
};