from keypad import KeyPad
import time
         
keyPad=KeyPad(15,2,0,4,5,14,12,13)

def key():
    keyvalue=keyPad.scan()
    if keyvalue!= None:
        print(keyvalue)
        time.sleep_ms(300)
        return keyvalue
try:            
   while True:
       key()
except:
    pass
    
    
    
    
    
    
    