from machine import Pin,PWM
import math
import time

PI=3.14
button=Pin(4,Pin.IN,Pin.PULL_UP)
passiveBuzzer=PWM(Pin(5),1000)

def alert():
    for x in range(0,36):
        sinVal=math.sin(x*(PI/180))
        toneVal=500+int(sinVal*500)
        passiveBuzzer.duty(1000)
        passiveBuzzer.freq(toneVal)
        print("Running ",toneVal)
        time.sleep_ms(10)
try:
    while True:
        if not button.value():            
             passiveBuzzer.init()
             alert()   
        else:
            passiveBuzzer.duty(0)
            passiveBuzzer.deinit()
except:
    passiveBuzzer.deinit()
