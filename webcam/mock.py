from webcam.feeder import *
import glob, os
import PIL as pil
import numpy as np

class Mock(Feeder):
    def __init__(self):
        # Grab a list of files
        self.files = []
        self.index = 0

        path = "data/mock_images"
        if not os.path.isdir(path):
            print("No images in path: ", path)
            return

        for file in glob.glob(os.path.join(path, "*.bmp")):
            self.files.append(file)

    def next(self):
        input("Press enter mock file " + str(self.index))
        if self.index >= len(self.files):
            return None

        file = self.files[self.index]
        with pil.Image.open(file) as img:
            w, h = img.size
            data = []

            for x in range(w):
                for y in range(h):
                    data.append(img.getpixel((x, y)))

        self.index += 1
        self.index = self.index % len(self.files)
        return np.array(data)