class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        firstWord = ''.join([str(ord(x) - 97) for x in firstWord])
        secondWord = ''.join([str(ord(x) - 97) for x in secondWord])
        targetWord = ''.join([str(ord(x) - 97) for x in targetWord])
        return int(firstWord) + int(secondWord) == int(targetWord)