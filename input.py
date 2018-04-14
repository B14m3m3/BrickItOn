class Input:
    def __init__(self, charIndex):
        self.index = charIndex
        self.char = chr(97 + charIndex)

    def __str__(self):
        return "Input: " + str(self.index) + " => " + self.char