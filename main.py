import webcam as wb
import brain
from input import *
import argparse


class Program:
    def __init__(self):
        # Use command line arguments to decide if we should mock
        self.feeder = (wb.mock.Mock() if flags.mock_camera else wb.hand.Hand())
        self.detector = (brain.mock.Mock() if flags.mock_brain else brain.detector.Detector())

    def train(self):
        print("Training...")
        brain.tensor_train.Trainer().run()

    def guess(self):
        filename = "brain/dataset/sign_mnist_test_abcg_small.csv"
        print("Guessing using file", filename)
        print("Result is: ", self.detector.guessFromFile(filename))


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

            if (command != None):
                self.commandRobot(command)


# Parse commands args
parser = argparse.ArgumentParser()
parser.add_argument("-train", help="Start training the tensorflow model", action="store_true")
parser.add_argument("-validate", help="Run validation tests on hardcoded validation set", action="store_true")
parser.add_argument("-mock-camera", help="Mock data from camera", action="store_true")
parser.add_argument("-mock-brain", help="Mock brain analysis (tensorflow)", action="store_true")
flags = parser.parse_args()

prg = Program()

if flags.train:
    prg.train()
elif flags.validate:
    prg.guess()
else:
    prg.run()
