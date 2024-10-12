class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpha = {}
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i, n in enumerate(morse):
            alpha[chr(97 + i)] = n
            
        res = set()

        for i in words:
            for j in i:
                i = i.replace(j,alpha[j])
            res.add(i)
            
        return len(res)