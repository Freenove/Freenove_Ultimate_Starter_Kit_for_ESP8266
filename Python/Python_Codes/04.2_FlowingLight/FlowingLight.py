from machine import Pin,PWM
import time
pins=[13, 12, 14, 5, 4, 0, 2, 15]
dutys=[0,0,0,0,0,0,0,0,1023,512,256,128,64,32,16,8,0,0,0,0,0,0,0,0];
delayTimes=50
frequency = 1000
def showled():                              
    for i in range(0,16):
        for j in range(0,8):
           led = PWM(Pin(pins[j]),frequency)
           led.duty(dutys[i+j])
        time.sleep_ms(delayTimes)           
    for i in range(0,16):
        for j in range(0,8):
           led = PWM(Pin(pins[7-j]),frequency)
           led.duty(dutys[i+j])
        time.sleep_ms(delayTimes)
while True:
    showled()
