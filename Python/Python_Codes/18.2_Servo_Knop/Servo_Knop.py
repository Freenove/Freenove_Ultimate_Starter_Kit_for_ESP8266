from myservo import myServo
from machine import ADC,Pin
import time

servo=myServo(15)

adc=ADC(0)

try:
    while True:
        adcValue=adc.read()
        angle=(adcValue*180)/1024
        servo.myServoWriteAngle(int(angle))
        time.sleep_ms(50)
except:
    servo.deinit()