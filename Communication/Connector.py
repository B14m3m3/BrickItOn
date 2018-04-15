import socket

class Connector:
    
    def __init__(self):
        address = "192.168.0.1"
        port = "44446"
        self.s = socket.socket()
        self.s.connect(address, port)
        print("connection established")

    def forward(self):
        self.s.send("forward")

    def back(self):
        self.s.send("back")

    def turn_right(self):
        self.s.send("right")

    def turn_left(self):
        self.s.send("left")

    def stop(self):
        self.s.send("stop")

if __name__ == '__main__':
    con = Connector()
    con.forward()
