import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norme(self):
        x = math.sqrt(self.x**2 + self.y**2)
        return x