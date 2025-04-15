import math
class SodaCan:
    def __init__(self, dim1,  dim2):
        self._raggio = dim1
        self._altezza = dim2
    def getSurfaceArea(self):
        return 2 * math.pi * self._raggio * self._altezza + 2 * math.pi * self._raggio**2
    def getVolume(self):
        return math.pi * self._raggio**2 * self._altezza

mini_lattina= SodaCan(2.5, 7.6)

print(mini_lattina.getSurfaceArea())
print(mini_lattina.getVolume())