import webcam as wb
import brain
from input import *
import argparse
import Communication as comm
import game
import gui

class Program:
    def __init__(self):
        # Use command line arguments to decide if we should mock
        self.feeder = (wb.mock.Mock() if flags.mock_camera else wb.hand.Hand())
        self.detector = (brain.mock.Mock() if flags.mock_brain else brain.detector.Detector())

        # Setup game
        if flags.game:
            connector = comm.Connector.Connector(flags.ip, flags.port)
            self.game = game.controller.GameController(connector)
        else:
            self.game = None

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

    def processFromGUI(self, imgdata):
        if imgdata is None:
            return None

        command = self.detector.guess(imgdata.flatten())
        self.commandRobot(command)


    def commandRobot(self, command):
        if self.game is not None:
            self.game.onInput(command)

    def run(self):
        while True:
            command = self.fetchNextCommand()

            if (command is not None):
                self.commandRobot(command)


# Parse commands args
parser = argparse.ArgumentParser()
parser.add_argument("-train", help="Start training the tensorflow model", action="store_true")
parser.add_argument("-validate", help="Run validation tests on hardcoded validation set", action="store_true")
parser.add_argument("-mock-camera", help="Mock data from camera", action="store_true")
parser.add_argument("-mock-brain", help="Mock brain analysis (tensorflow)", action="store_true")
parser.add_argument('-ip', help='IP address of robot', default="192.168.0.1")
parser.add_argument('-port', type=int, help='Port of robot', default=44446)
parser.add_argument("-gui", help="Display GUI", action="store_true", default=True)
parser.add_argument("-game", help="Run the game", action="store_true", default=True)
flags = parser.parse_args()

prg = Program()
if flags.train:
    prg.train()
elif flags.gui:
    gui.interface.Interface.show(prg)
elif flags.validate:
    prg.guess()
else:
    prg.run()
