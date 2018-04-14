import webcam.hand as hand
import brain.detector as dect
from input import *

class Program:
    def __init__(self):
        self.feeder = hand.Hand()
        self.detector = dect.Detector()

    def train(self):
        print("Training...")

    def fetchNextCommand(self):
        imgdata = self.feeder.next().flatten()
        command = self.detector.guess(imgdata)
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