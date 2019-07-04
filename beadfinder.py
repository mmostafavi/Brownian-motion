import sys
from blob import Blob
from picture import Picture


class Beadfinder:
    def __init__(self, picture, tau):

        w = picture.width()
        h = picture.height()
        conditon = [None]*h
        pic = [None]*h
        blobs = []

        # creating two w*h array
        for i in range(h):
            pic[i] = [0]*w
            conditon[i] = [False]*w

        # lumanance is for specifing
        # a pixel as a bead or water
        def lumanance(c):
            r = c.getRed()
            g = c.getGreen()
            b = c.getBlue()
            return 0.299*r + 0.587*g + 0.114*b

        for row in range(h):
            for col in range(w):
                c = picture.get(col, row)
                brightness = int(round(lumanance(c)))
                if brightness >= tau:
                    pic[row][col] = 1

        # blobfinder is recursive function
        # that group the beads near to each
        # other as a "blob"

        def blobfinder(pic, condition, blob, row, col):
            if row < 0 or row >= h or col < 0 or col >= w:
                return
            if pic[row][col] == 0:
                return
            elif condition[row][col]:
                return

            blob.add(col, row)
            condition[row][col] = True

            blobfinder(pic, condition, blob, row - 1, col)
            blobfinder(pic, condition, blob, row + 1, col)
            blobfinder(pic, condition, blob, row, col + 1)
            blobfinder(pic, condition, blob, row, col - 1)

        # finding blobs with searching in all
        # pixels of a picture
        for row in range(h):
            for col in range(w):
                if not conditon[row][col] and pic[row][col] == 1:
                    blob = Blob()
                    blobfinder(pic, conditon, blob, row, col)
                    blobs.append(blob)
        self.blobs = blobs

    # filtering blobs based on their
    # mass in comparision with min_pixels
    def getBeads(self, min_pixels):
        blobs = self.blobs[:]
        for i in range(len(blobs) - 1, -1, -1):
            if blobs[i].mass() < min_pixels:
                del blobs[i]
        return blobs


def __main__():
    min_pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    filename = sys.argv[3]
    picture = Picture(filename)
    bead = Beadfinder(picture, tau)
    beads = bead.getBeads(min_pixels)
    print(len(beads))
    for b in beads:
        print(str(b))


if __name__ == "__main__":
    __main__()
