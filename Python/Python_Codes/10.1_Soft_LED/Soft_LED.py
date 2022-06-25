from machine import ADC, Pin, PWM
import time
adc = ADC(0)
pwm = PWM(Pin(4))
pwm.freq(1000)
try:
    while True:
        adcValue = adc.read()
        pwm.duty(adcValue)
        time.sleep(0.1)
except:
    pwm.deinit()





