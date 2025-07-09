import time

steps = 0

def move_R():
    global steps
    while steps < 10:
        steps += 1
        time.sleep(0.3)
        print(f"{' ' * steps}-*-")

def move_L():
    global steps
    while steps > 0:
        steps -= 1
        time.sleep(0.3)
        print(f"{' ' * steps}-*-")

try:
    while True:
        move_R()
        move_L()
except KeyboardInterrupt:
    print("Good bye")
