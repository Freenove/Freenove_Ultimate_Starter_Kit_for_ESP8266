from machine import Pin,PWM,ADC
import time

pwm0=PWM(Pin(13,Pin.OUT),1000)
pwm1=PWM(Pin(14,Pin.OUT),1000)
pwm2=PWM(Pin(12,Pin.OUT),1000)
adc0=ADC(0)
def setColor(r, g, b):
    pwm0.duty(r)
    pwm1.duty(g)
    pwm2.duty(b)
    time.sleep_ms(100)
try:
    while True:
        adcValue=adc0.read()

        if(adcValue>=0) and (adcValue<=345):
            setColor(1023, 0, 1023)
        elif (adcValue>345) and (adcValue<680):    
            setColor(0, 1023, 1023)
        elif(adcValue>=680) and (adcValue<=1024):    
            setColor(1023, 1023, 0)        
except:
    pwm0.deinit()
    pwm1.deinit()
    pwm2.deinit()