import input as inp

class Mock:
    def __init__(self):
        self.index = 0
        self.data = [
            'a',
            'b',
            'c',
            'g'
        ]

    def fill(self, chars):
        self.data = chars;

    def guess(self, imagepixels):
        num = len(self.data)
        if self.index >= num:
            self.index = 0

        if num == 0:
            raise Exception("Ingen mockup-data defineret til brain/mock.py!")

        # Create input object
        res = inp.Input(ord(self.data[self.index]) - 97)
        self.index += 1

        return res
