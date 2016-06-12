from ServoControl import *

s = Servo(21)

for i in range(10):
    s.moveLeft()
    time.sleep(1)
    s.moveRight()
    time.sleep(1)

s.stop()
