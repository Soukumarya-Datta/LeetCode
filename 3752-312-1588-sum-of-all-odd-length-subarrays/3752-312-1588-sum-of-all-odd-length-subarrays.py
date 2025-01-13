class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:        
        sum = 0 
        freq = 0
        for i in range(len(arr)):
            freq = freq-(i+1)//2+(len(arr)-i+1)//2
            sum += freq*arr[i]
        return sum