from machine import Pin, SoftSPI
from mfrc522 import MFRC522

sck = Pin(14, Pin.OUT)
copi = Pin(13, Pin.OUT) # Controller out, peripheral in
cipo = Pin(12, Pin.OUT) # Controller in, peripheral out
spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=copi, miso=cipo)
sda = Pin(4, Pin.OUT)
reader = MFRC522(spi, sda)
key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

try:
    while True:
        (status, tag_type) = reader.request(reader.CARD_REQIDL)#Read the card type number
        if status == reader.OK:
            print('Find the card!')
            (status, raw_uid) = reader.anticoll()#Reads the card serial number of the selected card
            if status == reader.OK:
                print('New Card Detected')
                print('  - Tag Type: 0x%02x' % tag_type)
                print('  - uid: 0x%02x%02x%02x%02x' % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                print('')
                if reader.select_tag(raw_uid) == reader.OK:#Read card memory capacity
                    reader.Read_Data(key, raw_uid)                
except KeyboardInterrupt:
        pass
    