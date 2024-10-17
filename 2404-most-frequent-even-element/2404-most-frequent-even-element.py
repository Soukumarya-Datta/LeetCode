class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d, max, res = {}, 0, -1; d_get = d.get

        for n in nums: 
            if n % 2 == 0: d[n] = d_get(n,0) + 1
        
        for num, count in d.items():
            if count >= max:
                if count > max: max = count; res = num
                else: res = min(num, res)

        return res