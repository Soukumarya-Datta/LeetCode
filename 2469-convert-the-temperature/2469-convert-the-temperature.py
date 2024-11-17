class Solution:
    def convertTemperature(self, c: float) -> List[float]:
        f = c * 1.8 +32
        k = c + 273.15
        return list([k,f])