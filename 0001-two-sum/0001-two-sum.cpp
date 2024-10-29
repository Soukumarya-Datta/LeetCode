class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> m;
        vector<int> v;
        for(int i=0;i<nums.size();i++)
        {
            if(m.find(target-nums[i])!=m.end())
            {
                auto it = m.find(target-nums[i]);
                v.push_back(i);
                v.push_back(it->second);
                break;
            }
            else
                m.insert(pair<int,int>(nums[i],i));
        }
        return v;
    }
};