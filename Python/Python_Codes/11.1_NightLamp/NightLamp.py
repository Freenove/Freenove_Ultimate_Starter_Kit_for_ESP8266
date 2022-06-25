from machine import Pin,PWM,ADC
import time

pwm =PWM(Pin(5,Pin.OUT),1000)
adc=ADC(0)

try:
    while True:
        adcValue=adc.read()
        pwm.duty(adcValue)
        print(adc.read())
        time.sleep_ms(100)
except:
    pwm.deinit()

