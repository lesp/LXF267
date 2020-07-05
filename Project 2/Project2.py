import explorerhat as eh
from time import sleep

try:
    while True:
        motor1y = round(eh.analog.one.read(),1)
        motor2y = round(eh.analog.two.read(),1)
        print(motor1y, motor2y)
        sleep(0.1)
        pulse1 = motor1y*5
        pulse2 = motor2y*5
        eh.light.pulse(pulse1,pulse1,pulse2,pulse2)
        eh.motor.one.speed(motor1y * 20.4)
        eh.motor.two.speed(motor2y * 20.4)
except KeyboardInterrupt:
    print("Exit")

