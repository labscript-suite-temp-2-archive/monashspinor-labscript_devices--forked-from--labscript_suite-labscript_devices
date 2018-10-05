from labscript_devices.NI_DAQmx.labscript_devices import NI_PCI_6733, NI_USB_6008
from labscript_devices.PulseBlasterUSB import PulseBlasterUSB

from labscript import (
    ClockLine,
    start,
    stop,
    labscript_init,
    AnalogOut,
    DigitalOut,
    StaticAnalogOut,
    StaticDigitalOut,
)

import sys
sys.excepthook = sys.__excepthook__

# labscript_init('test.h5', new=True, overwrite=True)
PulseBlasterUSB('pulseblaster')
ClockLine('clock', pulseblaster.pseudoclock, 'flag 0')
NI_PCI_6733('Dev1', clock, clock_terminal='PFI0')
NI_USB_6008('Dev3', num_AI=0)


AnalogOut('ao0', Dev1, 'ao0')
AnalogOut('ao1', Dev1, 'ao1')

DigitalOut('do0', Dev1, 'port0/line0')
DigitalOut('do1', Dev1, 'port0/line1')

StaticAnalogOut('static_ao0', Dev3, 'ao0')
StaticAnalogOut('static_ao1', Dev3, 'ao1')

StaticDigitalOut('static_do0', Dev3, 'port0/line0')
StaticDigitalOut('static_do1', Dev3, 'port1/line1')

start()

static_ao0.constant(3)
static_ao1.constant(2)
static_do0.go_high()
static_do1.go_high()

t = 0
ao0.constant(t, 3)
t += 1
t += ao0.ramp(t, duration=1, initial=1, final=10, samplerate=5)
do1.go_high(t)
stop(t+1)
# import os
# os.system('hdfview test.h5 > /dev/null')