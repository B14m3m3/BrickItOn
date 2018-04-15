import socket
import sys
import time
import ev3dev.ev3 as ev3

print(":: Starting program :: \n")

ma = ev3.LargeMotor('outA')
mb = ev3.LargeMotor('outD')
c = None

print(":: Motors ready :: \n")



def not_supported(*args, **kwargs):
    print("Not supported")


def move_forward(time, speed):
    ma.run_timed(time_sp=time, speed_sp=speed)
    mb.run_timed(time_sp=time, speed_sp=speed)


def move_backwards(time, speed):
    ma.run_timed(time_sp=time, speed_sp=-speed)
    mb.run_timed(time_sp=time, speed_sp=-speed)


def move_left(time, speed):
    ma.run_timed(time_sp=time, speed_sp=speed)
    mb.run_timed(time_sp=time, speed_sp=-speed)


def move_right(time, speed):
    mb.run_timed(time_sp=time, speed_sp=speed)
    ma.run_timed(time_sp=time, speed_sp=-speed)


def stop(*args, **kwargs):
    print("STOP hammertime")
    ma.stop()
    mb.stop()


def switch(argument):
    argument = argument.rstrip()
    print(argument)
    if argument == "forward":
        move_forward(500, 500)
    elif argument == "back":
        move_backwards(500, 500)
    elif argument == "right":
        move_right(500, 500)
    elif argument == "left":
        move_left(500, 500)
    elif argument == "stop":
        stop(500, 500)
    else:
        not_supported(500, 500)


def initializeServer():
    s = socket.socket()  # Create a socket object
    host = '0.0.0.0'  # Get local machine name
    port = 44446  # Reserve a port for your service.
    s.bind((host, port))  # Bind to the port
    print(host)
    s.listen(5)  # Now wait for client connection.

    while True:
        print("Listening for client")
        c, addr = s.accept()  # Establish connection with client.
        print("Client connected, waiting for input")
        handleClient(c)

def handleClient(c):
    while True:
        try:
            argument = c.recv(1024)
            switch(argument.decode())
        except:
            print("Unexpected error:", sys.exc_info()[0])
            break
    c.close()

initializeServer()
