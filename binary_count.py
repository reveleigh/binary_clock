from neopixel import Neopixel
import utime

numpix = 16
strip = Neopixel(numpix, 0, 22, "GRB")
red = (255, 0, 0)
white = (255, 255, 255)
strip.brightness(100)


blank = (0,0,0)


def one(x):
    for i in range(0,2):
        if x == 1:
            strip.set_pixel(i, white)
        else:
            strip.set_pixel(i, red)
    
def two(x):
    for i in range(2,4):
        if x == 1:
            strip.set_pixel(i, white)
        else:
            strip.set_pixel(i, red)

def four(x):
    for i in range(4,6):
        if x == 1:
            strip.set_pixel(i, white)
        else:
            strip.set_pixel(i, red)

def eight(x):
    for i in range(6,8):
        if x == 1:
            strip.set_pixel(i, white)
        else:
            strip.set_pixel(i, red)

def sixteen(x):
    for i in range(8,10):
        if x == 1:
            strip.set_pixel(i, white)
        else:
            strip.set_pixel(i, red)

def thirtytwo(x):
    for i in range(10,12):
        if x == 1:
            strip.set_pixel(i, white)
        else:
            strip.set_pixel(i, red)

def sixtyfour(x):
    for i in range(12,14):
        if x == 1:
            strip.set_pixel(i, white)
        else:
            strip.set_pixel(i, red)

def onetwoeight(x):
    for i in range(14,16):
        if x == 1:
            strip.set_pixel(i, white)
        else:
            strip.set_pixel(i, red)


def decToBinary(n):
    y = n
    if y >= 128:
        onetwoeight(1)
        y = y - 128
    else:
        onetwoeight(0)
    if y >= 64:
        sixtyfour(1)
        y = y - 64
    else:
        sixtyfour(0)
    if y >= 32:
        thirtytwo(1)
        y = y - 32
    else:
        thirtytwo(0)
    if y >= 16:
        sixteen(1)
        y = y - 16
    else:
        sixteen(0)
    if y >= 8:
        eight(1)
        y = y - 8
    else:
        eight(0)
    if y >= 4:
        four(1)
        y = y - 4
    else:
        four(0)
    if y >= 2:
        two(1)
        y = y - 2
    else:
        two(0)
    if y >= 1:
        one(1)
        y = y - 1
    else:
        one(0)
    strip.show()

count = 0

while count < 256:
    decToBinary(count)
    utime.sleep(1)  
    count = count + 1
    if count == 256:
        count = 0

