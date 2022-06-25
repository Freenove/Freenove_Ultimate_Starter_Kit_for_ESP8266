from machine import Pin, SoftSPI
from mfrc522 import MFRC522

sck = Pin(14, Pin.OUT)
copi = Pin(13, Pin.OUT) # Controller out, peripheral in
cipo = Pin(12, Pin.OUT) # Controller in, peripheral out
spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=copi, miso=cipo)
sda = Pin(4, Pin.OUT)
reader = MFRC522(spi, sda)
key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
option = 0

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
                    while option != "7":
                        print("**Please enter the options**")
                        print("1: Read the card data")
                        print("2: Write data to the card")
                        print("3: Clear data")
                        print("4: Read a row of data")
                        print("5: Write a line of data")
                        print("6: Clear a line of data")
                        print("7: Exit or Ctrl + C")
                        option = input("Input option: ")
                        print("")
                        if option == "1":
                            reader.Read_Data(key, raw_uid)
                        elif option == "2":
                            datas = input("plase input datas: ")
                            reader.Write_Data(key, raw_uid, datas)
                        elif option == "3":
                            reader.Clear_Data(key, raw_uid)
                        elif option == "4":
                            row_index = int(input("Please enter the row index: "))
                            if (row_index+1)%4 == 0 or row_index == 0 or row_index > 63:
                                print("\nPermission Denied")
                            if reader.auth(0x60, row_index, key, raw_uid) == reader.OK:  #Verification card password
                                if bytearray(reader.read(row_index)) == bytearray(16):
                                     print("No Data")
                                else:
                                    print(str(row_index) + ": " + str(bytearray(reader.read(row_index)).decode()))
                            else:
                                print("ERROR")
                        elif option == "5":
                            row_index = int(input("Please enter the row index: "))
                            datas = input("plase input datas: ")
                            reader.Write_Row_Data(key, raw_uid, row_index, datas)
                        elif option == "6":
                            row_index = int(input("Please enter the row index: "))
                            reader.Clear_Row_Data(key, raw_uid, row_index)
                        elif option == "7":
                            reader.stop_crypto1()
                            print("Exit the success")
                        else:
                            print("Input error")
                        print("")
                    break
except KeyboardInterrupt:
    pass
