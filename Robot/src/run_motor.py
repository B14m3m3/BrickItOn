import ev3dev.ev3 as ev3
import time

ma = ev3.LargeMotor('outA')
mb = ev3.LargeMotor('outD')


dir(ev3)

def move_forward(time, speed):
    ma.run_timed(time_sp=time, speed_sp=speed)
    mb.run_timed(time_sp=time, speed_sp=speed)

def move_backwards(time, speed):
    ma.run_timed(time_sp=time, speed_sp=-speed)
    mb.run_timed(time_sp=time, speed_sp=-speed)

def move_left(time, speed):
    ma.run_timed(time_sp=time, speed_sp=speed)

def move_right(time, speed):
    mb.run_timed(time_sp=time, speed_sp=speed)

def stop():
    ma.stop()
    mb.stop()

# move_forward(5000, 500)
# move_left(5000, 500)
# move_backwards(3000, 500)


def switch_demo(argument):
    switcher = {
        'forward': move_forward(1000, 500),
        'back': move_backwards(1000, 500),
        'left': move_left(1000, 500),
        'right': move_right(1000, 500),
        'stop': stop()
    }
