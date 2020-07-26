from machine import Timer
from machine import Pin

# import pyb # module 'pyb' is not available on ESP32
import micropython
micropython.alloc_emergency_exception_buf(100)

tim = Timer(0) # use timer 1 (of 4)

# most ESP32 Boards don't have builtin LEDs, so an external LED is connected to GPIO33 (with 220 Ohm pullup resistor)
led = Pin(33, Pin.OUT)

def isr_timer(timer):           # we will receive the timer object when being called
    global led
    led.value(not led.value())  # toggle the LED

tim.init(mode=Timer.PERIODIC, period=100, callback=isr_timer)
