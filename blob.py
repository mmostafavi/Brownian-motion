import math


class Blob:
    def __init__(self):
        self.blob = []
        self.center = [0, 0]
        self.count = 0

    def add(self, x, y):
        self.center[0] = (self.center[0]*self.count + x)/(self.count + 1)
        self.center[1] = (self.center[1]*self.count + y)/(self.count + 1)
        self.blob.append([x, y])
        self.count += 1

    def mass(self):
        return self.count

    def distanceTo(self, b):
        logb = str(b)

        # find the index of ( in string
        openI = logb.find("(")

        # find the index of , in string
        commaI = logb.find(",", openI)

        # find the index of ) in string
        closeI = logb.find(")", commaI)

        bX = logb[openI + 1: commaI]
        bY = logb[commaI + 2: closeI]

        dx = float(bX) - self.center[0]
        dy = float(bY) - self.center[1]

        return math.sqrt(dx*dx + dy*dy)

    def __str__(self):
        return "%s (%.4f, %.4f)" % (self.count, self.center[0], self.center[1])


def __main__():
    blob1 = Blob()
    blob2 = Blob()
    blob1.add(10, 12)
    blob1.add(3, 5)
    blob2.add(2, 5)
    blob2.add(10, 10)
    print(blob1.mass())
    print(blob2.mass())
    print(blob1.distanceTo(blob2))
    print(str(blob1))


if __name__ == "__main__":
    __main__()
