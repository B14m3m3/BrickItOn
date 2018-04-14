from PIL import Image
import os

class Converter:
    def __init__(self, filename, is_train, limit = 0, targetPath = "images"):
        self.filename = filename
        self.is_train = is_train
        self.limit = limit
        self.targetPath = targetPath

        # Create target directory
        if not os.path.isdir(self.targetPath):
            os.makedirs(self.targetPath)

    def convert(self):
        self.counter = -1
        with open(self.filename) as f:
            for line in f:
                self.counter += 1
                if self.counter == 0:
                    continue
                if self.counter > self.limit:
                    break

                raw = line.strip().split(",") # First part is the hand signal
                self.storeImage(raw[0], raw[1:])

    def storeImage(self, signal, imgdata):
        img = Image.new('L', (28, 28))
        x = 0
        y = 0
        for val in imgdata:
            img.putpixel((x,y), int(val))
            x += 1
            x %= 28
            if(x == 0):
                y += 1

        char = chr(int(signal) + 97)
        img.save(os.path.join(self.targetPath, str(self.counter) + "_signal_" + char + ".bmp"))

conv = Converter("dataset/sign_mnist_test.csv", True, 100, targetPath="images/test")
conv.convert()