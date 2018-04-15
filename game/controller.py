class GameController:
    def __init__(self, connector):
        self.con = connector
        self.player = 0
        self.moves = [0, 0]

    def onInput(self, cmd):
        print("OnInput reached!")
        if cmd.isForward():
            self.con.forward()
        elif cmd.isBack():
            self.con.back()
        elif cmd.isRight():
            self.con.turn_right()
        elif cmd.isLeft():
            self.con.turn_left()

        self.moves[self.player] += 1

    def nextPlayer(self):
        self.player += 1
        self.moves[self.player] = 0

    def printStats(self):
        print(self.moves)
        #for p in self.moves:
        #    print("Player ", p, self.moves[p])
