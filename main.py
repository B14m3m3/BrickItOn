import webcam as wb
import brain
from input import *

class Program:
    def __init__(self):
        self.feeder = wb.mock.Mock() #wb.hand.Hand() for webcam
        self.detector = brain.mock.Mock()

    def train(self):
        print("Training...")

    def fetchNextCommand(self):
        imgdata = self.feeder.next()

        if imgdata is None:
            return None

        command = self.detector.guess(imgdata.flatten())
        return command

    def commandRobot(self, command):
        print("Commanding robot")
        pass

    def run(self):
        while True:
            command = self.fetchNextCommand()
            print(command)

            if(command != None):
                self.commandRobot(command)

# Parse commands args
prg = Program()
prg.run()