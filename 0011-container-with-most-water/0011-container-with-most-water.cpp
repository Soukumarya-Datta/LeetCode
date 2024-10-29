class Solution {
public:
    int maxArea(vector<int>& h) {
        int l = 0, r = h.size() - 1, maxArea = 0;
        while(l<r) {
            int area = min(h[l],h[r])*(r-l);
            maxArea = max(area, maxArea);
            (h[l]>h[r])?r--:l++;
        }
        return maxArea;
    }
};