import webcam as wb
import brain
from input import *
import argparse

class Program:
    def __init__(self):
        self.feeder = wb.mock.Mock() #wb.hand.Hand() for webcam
        self.detector = brain.mock.Mock()

    def train(self):
        print("Training...")
        brain.tensor_train.Trainer().run()

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
parser = argparse.ArgumentParser()
parser.add_argument("-train", help="Start training the tensorflow model", action="store_true")
args = parser.parse_args()

prg = Program()

if args.train:
    prg.train()
else:
    prg.run()