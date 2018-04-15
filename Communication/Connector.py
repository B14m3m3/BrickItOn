import socket

class Connector:
    
    def __init__(self, address, port=44446):
        print("Connecting to robot...")
        self.s = socket.socket()
        self.s.connect((address, port))
        print("Connection established")

    def write(self, msg):
        print("Sending to robot: ", msg)
        self.s.send(msg.encode())

    def forward(self):
        self.write("forward")

    def back(self):
        self.write("back")

    def turn_right(self):
        self.write("right")
    
    def turn_left(self):
        self.write("left")

    def stop(self):
        self.write("stop")

if __name__ == '__main__':
    con = Connector()
    con.forward()
