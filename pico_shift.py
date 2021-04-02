from machine import *
from utime import sleep
from math import log
class Shift:
    MSBfirst = True
    LSBfirst = False
    def __init__(self, clock, data, latch):
        self.clock_pin = Pin(clock, Pin.OUT)
        self.data_pin = Pin(data, Pin.OUT)
        self.latch_pin = Pin(latch, Pin.OUT)
    
    def latch(self, active_low=True):
        start = (1, 0)[active_low]
        self.latch_pin.value(start)
        self.latch_pin.value(1-start)
        self.latch_pin.value(start)
    
    def shift_bit(self, bit: int):
        if bit != 1 and bit != 0:
            raise ValueError("bit should be 0 or 1")
        else:
            self.data_pin.value(bit)
            self.clock_pin.value(0)
            self.clock_pin.value(1)
            self.clock_pin.value(0)

    def shift_byte(self, byte: int, mode=True):
        if byte < 0 or byte > 255:
            raise ValueError("byte should be between 0 and 255")
        else:
            for i in range(8):
                bit = (byte >> i if mode else byte >> 7-i) % 2
                self.shift_bit(bit)
    def shift_num(self, num, mode=True):
        """
        writes data to the shift register
        
        num: the data
        mode: MSBfirst or LSBfirst
        """
        #find the length of the number in binary
        length = int(log(num, 2)) + 1
        for i in range(length):
            bit = (num >> i if mode else num >> length-1-i) % 2
            self.data_pin.value(bit)
            #pulse clock to push bit to register
            self.clock_pin.value(0)
            self.clock_pin.value(1)
            self.clock_pin.value(0)
        
        #pulse latch to, well, latch
        #since latch is active low in the 74HC595, we'll unpulse it
        