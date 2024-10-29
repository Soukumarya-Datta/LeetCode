class Solution {
public:
    void findNumber(vector<int> &a, int sum, int i, vector<int> &r,vector<vector<int>> &res){
        if(sum<0) return;
        if(sum == 0){
            res.push_back(r);
            return;
        }
        while(i<a.size() && sum-a[i]>=0){
            r.push_back(a[i]);
            findNumber(a,sum-a[i],i,r,res);
            i++;
            r.pop_back();
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> r;
        sort(candidates.begin(),candidates.end());
        candidates.erase(unique(candidates.begin(),candidates.end()),candidates.end());
        vector<vector<int>> res;
        findNumber(candidates,target,0,r,res);
        return res;
    }   
};