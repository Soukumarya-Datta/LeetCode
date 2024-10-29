class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& n) {
        int c=0,maxi=INT_MIN;
        for(int i=0;i<n.size();i++)
        {
            if(n[i]==1)
                c++;
            if(n[i]!=1 || i==n.size()-1)
            {
                maxi=max(c,maxi);
                c=0;
            }
        }
        return maxi;
    }
};