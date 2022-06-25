from machine import ADC, Pin
import time

adc = ADC(0)

try:
    while True:
        adcValue = adc.read()
        voltage = adcValue / 1024.0 * 3.3
        print("ADC Value:", adcValue, "Voltage:", voltage, "V")
        time.sleep(0.1)
except:
    pass


