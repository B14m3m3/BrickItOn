class Input:
    def __init__(self, charIndex):
        self.index = charIndex
        self.char = chr(97 + charIndex)

    def isRight(self):
        return self.char == 'g'

    def isLeft(self):
        return self.char == 'c'

    def isForward(self):
        return self.char == 'b'

    def isBack(self):
        return self.char == 'a'

    def __str__(self):
        return "Input: " + str(self.index) + " => " + self.char