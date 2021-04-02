PicoShift
======

This is a simple library for interaction between the raspberry pi pico and shift registers such as the 74HC595. 

Usage
------
* download the .py file
* open Thonny or any IDE you use for the pico
* upload the file to the pico
* now you can use it using the documentation below (you can also just read the source code, it's very short, simple and commented)

To start you're going to need to define your register using the construtor ```shifty = Shift([clock pin number], [data pin number], [latch pin number])```.

Then you can write to it using one of these:

### shift_byte
This is the one I reccomend for most uses, and as the name suggests, it writes a byte to the shift register:
```shifty.shift_byte(number, mode=True)```

Where mode is either Shift.MSBfirst or Shift.LSBfirst, and the default is MSB.

### shift_number
This one shift out the number, but only to its length, so if you want to write 17 it will only shift those 5 bits. This may result in old data from prevoius writes staying on the register, but I've stumbled across some use cases for this behavior too. It takes the same parameters as shift_byte


After writing to the register you'll need to latch it, which you can do with ```latch(active_low=True)``` If your register has an active high latch pin you can set active_low to False, and it will pulse it to get the data to the output of the register

Example
-----
```python
from pico_shift import Shift

shifty = Shift(0, 1, 2)
shifty.shift_byte(0x55, Shift.MSBfirst)
shifty.latch()
shifty.shift_number(13, Shift.LSBfirst)
shifty.latch()
```
This example was written for a 74HC595 where GPIO0 was connected to pin 11 on the 595, GPIO1 is connected to pin 14 and GPIO2 is connected to pin 12.