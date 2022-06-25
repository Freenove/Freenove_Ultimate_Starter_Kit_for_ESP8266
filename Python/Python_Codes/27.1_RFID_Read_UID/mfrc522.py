from machine import Pin, SPI
from os import uname
MFRC522_DIVL_EN_REG                = 0x03   
class MFRC522(object):
    OK                             = 0
    NO_TAG_ERR                     = 1
    ERR                            = 2
    CARD_REQIDL                    = 0x26
    AUTH                           = 0x60
    def __init__(self, spi, cs):
        self.spi = spi
        self.cs = cs
        self.cs.value(1)
        self.spi.init()
        self.init()
    def _write_reg(self, reg, val):
        self.cs.value(0)
        self.spi.write(b'%c' % int(0xff & ((reg << 1) & 0x7e)))
        self.spi.write(b'%c' % int(0xff & val))
        self.cs.value(1)
    def _read_reg(self, reg):
        self.cs.value(0)
        self.spi.write(b'%c' % int(0xff & (((reg << 1) & 0x7e) | 0x80)))
        val = self.spi.read(1)
        self.cs.value(1)
        return val[0]
    def _set_bit_mask(self, reg, mask):
        self._write_reg(reg, self._read_reg(reg) | mask)
    def _clear_bit_mask(self, reg, mask):
        self._write_reg(reg, self._read_reg(reg) & (~mask))
    def _tocard(self, cmd, send):
        recv = []
        bits = irq_en = wait_irq = n = 0
        status = self.ERR
        if cmd == 0x0E:
            irq_en = 0x12
            wait_irq = 0x10
        elif cmd == 0x0C:
            irq_en = 0x77
            wait_irq = 0x30
        self._write_reg(0x02, irq_en | 0x80)
        self._clear_bit_mask(0x04, 0x80)
        self._set_bit_mask(0x0A, 0x80)
        self._write_reg(0x01, 0x00)
        for c in send:
            self._write_reg(0x09, c)
        self._write_reg(0x01, cmd)
        if cmd == 0x0C:
            self._set_bit_mask(0x0D, 0x80)
        i = 2000
        while True:
            n = self._read_reg(0x04)
            i -= 1
            if ~((i != 0) and ~(n & 0x01) and ~(n & wait_irq)):
                break
        self._clear_bit_mask(0x0D, 0x80)
        if i:
            if (self._read_reg(0x06) & 0x1B) == 0x00:
                status = self.OK
                if n & irq_en & 0x01:
                    status = self.NO_TAG_ERR
                elif cmd == 0x0C:
                    n = self._read_reg(0x0A)
                    last_bits = self._read_reg(0x0C) & 0x07
                    if last_bits != 0:
                        bits = (n - 1) * 8 + last_bits
                    else:
                        bits = n * 8
                    if n == 0:
                        n = 1
                    elif n > 16:
                        n = 16
                    for _ in range(n):
                        recv.append(self._read_reg(0x09))
            else:
                status = self.ERR
        return status, recv, bits

    def _calculate_crc(self, data):
        self._clear_bit_mask(0x05, 0x04)
        self._set_bit_mask(0x0A, 0x80)
        for c in data:
            self._write_reg(0x09, c)
        self._write_reg(0x01, 0x03)
        i = 0xFF
        while True:
            n = self._read_reg(0x05)
            i -= 1
            if not ((i != 0) and not (n & 0x04)):
                break
        return [self._read_reg(0x22), self._read_reg(0x21)]
    def init(self):
        self.reset()
        self._write_reg(0x2A, 0x8D)
        self._write_reg(0x2B, 0x3E)
        self._write_reg(0x2D, 30)
        self._write_reg(0x2C, 0)
        self._write_reg(0x15, 0x40)
        self._write_reg(0x11, 0x3D)
        self.antenna_on()
    def reset(self):
        self._write_reg(0x01, 0x0F)
    def antenna_on(self, on=True):
        if on and ~(self._read_reg(0x14) & 0x03):
            self._set_bit_mask(0x14, 0x03)
        else:
            self._clear_bit_mask(0x14, 0x03)
    def request(self, mode):
        self._write_reg(0x0D, 0x07)
        (status, recv, bits) = self._tocard(0x0C, [mode])
        if (status != self.OK) | (bits != 0x10):
            status = self.ERR
        return status, bits
    def anticoll(self):
        serial_number_check = 0
        serial_number = [0x93, 0x20]
        self._write_reg(0x0D, 0x00)
        (status, recv, bits) = self._tocard(0x0C, serial_number)
        if status == self.OK:
            if len(recv) == 5:
                for i in range(4):
                    serial_number_check = serial_number_check ^ recv[i]
                if serial_number_check != recv[4]:
                    status = self.ERR
            else:
                status = self.ERR
        return status, recv

    def select_tag(self, serial_number):
        buffer = [0x93, 0x70] + serial_number[:5]
        buffer += self._calculate_crc(buffer)
        (status, recv, bits) = self._tocard(0x0C, buffer)
        return self.OK if (status == self.OK) and (bits == 0x18) else self.ERR
    def auth(self, mode, addr, sect, serial_number):
        return self._tocard(0x0E, [mode, addr] + sect + serial_number[:4])[0]
    def stop_crypto1(self):
        self._clear_bit_mask(0x08, 0x08)
    def read(self, addr):
        data = [0x30, addr]
        data += self._calculate_crc(data)
        (status, recv, bits1) = self._tocard(0x0C, data)
        if ((status != self.OK) or not (bits1 != 0x90)):
            status = self.ERR
        return recv  
        
    def write(self, addr, data):
        buffer = [0xA0, addr]
        buffer += self._calculate_crc(buffer)
        (status, recv, bits) = self._tocard(0x0C, buffer)
        if not (status == self.OK) or not (bits == 4) or not ((recv[0] & 0x0F) == 0x0A):
            status = self.ERR
        else:
            buffer = []
            for i in range(16):
                buffer.append(data[i])
            buffer += self._calculate_crc(buffer)
            (status, recv, bits) = self._tocard(0x0C, buffer)
            if not (status == self.OK) or not (bits == 4) or not ((recv[0] & 0x0F) == 0x0A):
                status = self.ERR
        return status    
    def Read_Data(self, sect, serial_number):
        index = 0
        for i in range(1, 64):
            if (i+1)%4 != 0:
                if self.auth(self.AUTH, i, sect, serial_number) == self.OK:#Verification card password
                    if bytearray(self.read(i)) == bytearray(16):
                        index += 1
                        continue
                    else:
                        print(str(i) + ": " + str(bytearray(self.read(i)).decode()))
                else:
                    return
        if index == 64-17:
            print("No Data!")
        return    
    def Write_Data(self, sect, serial_number, datas):
        data = datas.encode()
        dataRow = len(data)//16
        if dataRow == 64-17:
            print("error")
            return
        endRow = len(data) % 16
        index = 0 
        for i in range(1, 64):
            if (i+1)%4 != 0:
                if self.auth(self.AUTH, i, sect, serial_number) == self.OK:#Verification card password
                    if dataRow == index and endRow != 0:
                        status = self.write(i, data[0+16*index : len(data)] + bytes(16 - endRow))
                        break
                    elif dataRow == index and endRow == 0:
                        break
                    else:
                        status = self.write(i, data[0+16*index : 16 + 16*index])
                    index += 1
                else:
                    print("AUTH ERROR")
                    return
        if status is self.OK:
            print("Write card OK!")
            return
    
    def Clear_Data(self, sect, serial_number):
        for i in range(1, 64):
            if (i+1)%4 != 0:
                if self.auth(self.AUTH, i, sect, serial_number) == self.OK:#Verification card password
                    status = self.write(i, bytearray(16))
                else:
                    print("AUTH ERROR")
        if status is self.OK:
            print("Clear Data!")
            return
    def Clear_Row_Data(self, sect, serial_number, addr):
        if (addr+1)%4 == 0 or addr == 0 or addr > 63:
            print("\nPermission Denied")
            return
        if self.auth(self.AUTH, addr, sect, serial_number) == self.OK:
            status = self.write(addr, bytearray(16))
            if status is self.OK:
                print("Clear Data!")
                return
        else:
            print("AUTH ERROR")
            return       
    def Write_Row_Data(self, sect, serial_number, addr, datas):
        if (addr+1)%4 == 0 or addr == 0 or addr > 63:
            print("\nPermission Denied")
            return
        if self.auth(self.AUTH, addr, sect, serial_number) == self.OK:
            data = datas.encode()
            if len(data) > 16 or len(data) == 0:
                return
            if len(data) == 16:
                status = self.write(addr, data[0 : 16])
            else:
                status = self.write(addr, data[0 : len(data)] + bytes(16 - (len(data)%16)))
            if status is self.OK:
                print("Write Data!")
                return
        else:
            print("AUTH ERROR")
            return


