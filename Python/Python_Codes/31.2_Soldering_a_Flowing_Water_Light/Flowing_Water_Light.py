import time
from my74HC595 import Chip74HC595

chip = Chip74HC595(14,12,13)
# ESP8266-14: 74HC595-DS(14)
# ESP8266-12: 74HC595-STCP(12)
# ESP8266-13: 74HC595-SHCP(11)

while True:
    x=0x01
    for count in range(8):
        chip.shiftOut(1,x)  #High bit is sent first
        x=x<<1
        time.sleep_ms(100)  
    x=0x01
    for count in range(8):
        chip.shiftOut(0,x)  #Low bit is sent first
        x=x<<1
        time.sleep_ms(100)
