from machine import Pin,ADC
import time
import math

adc=ADC(0)

try:
    while True:
        adcValue=adc.read()
        voltage=adcValue/1023*3.3
        Rt=10*voltage/(3.3-voltage)
        tempK=(1/(1/(273.15+25)+(math.log(Rt/10))/3950))
        tempC=tempK-273.15
        print("ADC value:",adcValue,"\tVoltage :",voltage,"\tTemperature :",tempC);
        time.sleep_ms(1000)
except:
    pass
