class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        for(int i = 0; i<nums2.size(); i++)
        nums1.push_back(nums2[i]);
        sort(nums1.begin(),nums1.end());
        double(ans);
        if(nums1.size()%2==0)
        {
            ans = (double(nums1[nums1.size()/2]) + double(nums1[(nums1.size()/2)-1]))/2.0;
        }
        else ans = double(nums1[nums1.size()/2]);
        return ans;
    }
    
};