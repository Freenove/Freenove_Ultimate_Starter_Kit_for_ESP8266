from machine import ADC,Pin,PWM
import time
import math

in1Pin=Pin(12, Pin.OUT)
in2Pin=Pin(14, Pin.OUT)

enablePin=Pin(13, Pin.OUT)
pwm=PWM(enablePin,1000)
adc=ADC(0)

def driveMotor(dir,spd):
    if dir :
        in1Pin.value(1)
        in2Pin.value(0)
    else :
        in1Pin.value(0)
        in2Pin.value(1)
    pwm.duty(spd)
    
try:
    while True:
        potenVal = adc.read()
        rotationSpeed = potenVal - 512
        if (potenVal > 512):
            rotationDir = 1;
        else:
            rotationDir = 0;
        rotationSpeed=int(math.fabs((potenVal-511)*2)-1)
        driveMotor(rotationDir,rotationSpeed)
        time.sleep_ms(10)
except:
    pass
