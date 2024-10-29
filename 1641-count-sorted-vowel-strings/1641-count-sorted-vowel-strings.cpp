class Solution {
public:
    int countVowelStrings(int n) {
        array<int, 5> counts = { 1, 1, 1, 1, 1 };
        for(int i = 1; i < n; ++i)
        for(int j = 1; j < 5; ++j) 
        counts[j] += counts[j-1];
        return accumulate(counts.begin(), counts.end(), 0);
    }
};