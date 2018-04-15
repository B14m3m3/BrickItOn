class GameController:
    def __init__(self, connector):
        self.con = connector
        self.player = 0
        self.moves = [0, 0]

    def onInput(self, cmd):
        if cmd.isForward():
            self.con.forward()
        elif cmd.isBack():
            self.con.back()
        elif cmd.isRight():
            self.con.turn_right()
        elif cmd.isLeft():
            self.con.turn_left()

        self.moves[self.player] += 1

    def switchPlayer(self):
        self.player = 1 - self.player
        self.moves[self.player] = 0

    def getScore(self, player):
        return (self.moves[player] if player < len(self.moves) else 0)

    def restartGame(self):
        self.moves = [0,0];