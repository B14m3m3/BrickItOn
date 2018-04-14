from Webcam.feeder import *
from tensorflow.detector import *
from input import *

class Program:
    def __init__(self):
        self.feeder = Feeder()
        self.detector = Detector()

    def train(self):
        print("Training...")

    def fetchNextCommand(self):
        imgdata = self.feeder.next()
        command = self.detector.guess(imgdata)
        return command

    def commandRobot(self, command):
        print("Commanding robot")
        pass

    def run(self):
        while True:
            command = self.fetchNextCommand()
            if(command != None):
                self.commandRobot(command)

# Parse commands args
prg = Program()
prg.run()