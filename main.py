from machine import Pin
import time

button = Pin(0, Pin.IN, Pin.PULL_UP)
#camera = Pin(1, Pin.IN, Pin.PULL_DOWN)
relay = Pin(1, Pin.OUT)

M1A = 21 # GP21
M1B = 20 # GP20

M2A = 19 # GP19
M2B = 18 # GP18
 
step_count = 8
n = list(range(0, step_count)) # sequence

n[0] = [0,1,0,0]
n[1] = [0,1,0,1]
n[2] = [0,0,0,1]
n[3] = [1,0,0,1]
n[4] = [1,0,0,0]
n[5] = [1,0,1,0]
n[6] = [0,0,1,0]
n[7] = [0,1,1,0]
 
en1 = Pin(17, Pin.OUT)
en2 = Pin(16, Pin.OUT)

m1a = Pin(M1A,Pin.OUT)
m1b = Pin(M1B,Pin.OUT) 
m2a = Pin(M2A,Pin.OUT) 
m2b = Pin(M2B,Pin.OUT) 


def setStep(p1, p2, p3, p4):

    m1a(p1)
    m1b(p2)
    m2a(p3)
    m2b(p4)

 
def Forward(delay, steps):
    for i in range(steps):
        for j in range(step_count):
            setStep(n[j][0], n[j][1], n[j][2], n[j][3])
            time.sleep(delay)
 
def Backward(delay, steps):
    for i in range(steps):
        for j in reversed(range(step_count)):
            setStep(n[j][0], n[j][1], n[j][2], n[j][3])
            time.sleep(delay)
def photo():
    print("Take a photo")
    relay.value(0)
    time.sleep(0.1)
    relay.value(1)
    
motor = False

while True:
    rotation = 0
    if not button.value():
        print("Button Pressed")
        print(rotation)
        if motor is False:
            en1(1)
            en2(1)
            motor = True
        while rotation in range(0,49):
            rotation += 1
            photo()
            time.sleep(1)
            print(rotation)
            Forward(0.05,1)
            time.sleep(0.5)
    
    if motor is True:
        en1(0)
        en2(0)
        motor = False

