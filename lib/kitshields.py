from micropython import const
from machine import Pin

# Pin Assignments

# SPI
SPI_MOSI = const(38)
SPI_MISO = const(39)
SPI_CLK = const(40)

# I2C
I2C_SDA = const(12)
I2C_SCL = const(11)

# PIR
PIN_PIR = const(13)
PIR = Pin(PIN_PIR, Pin.IN, Pin.PULL_UP)

# RELAY
PIN_RELAY = const(41)
RELAY = Pin(PIN_RELAY, Pin.OUT, 0)

