class Solution:
    def convertTemperature(self, c: float) -> List[float]:
        return list([c + 273.15,c * 1.8 +32])