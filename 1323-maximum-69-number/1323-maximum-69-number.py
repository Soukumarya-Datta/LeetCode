class Solution:
    def maximum69Number (self, num: int) -> int:
        n = math.floor(math.log10(num)+1)
        for i in range(n):
            if str(num)[i] == '6':
                num += 10 ** (n-i-1) * 3
                return num
        return num