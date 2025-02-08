class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return num.bit_length() + bin(num).count('1') - 1 
        # position of the highest set bit + total set bits - 1