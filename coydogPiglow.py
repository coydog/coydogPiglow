# Python module for piglow peripheral for RaspberryPi.
# Initializes device, provides helper function. Initialization
# code taken from pimoroni's example script

from smbus import SMBus

debugLog = False;
# command register addresses for SN3218 IC
CMD_ENABLE_OUTPUT = 0x00
CMD_ENABLE_LEDS = 0x13
CMD_SET_PWM_VALUES = 0x01
CMD_UPDATE = 0x16

# TODO: Maybe this should go in a class __init__ member?
i2c_addr = 0x54 # i2c address of SN3218
i2c_bus = 1 # might be 0 on earliest Pi revisions?

def update_leds(values):
	if debugLog:
		print "update_leds() " + str(values)
	write_i2c(CMD_SET_PWM_VALUES, values)
	write_i2c(CMD_UPDATE, 0xFF)

# TODO: API to update a single or group of LED's, but keep 
# state of others. Will track state in the module (or as a 
# class member)

# TODO: "fade in" - give a range to fade across and a time.
# Might can do logarithmic fading.

# intended as internal interface
def write_i2c(reg_addr, value):
	# if single value, make it a list
	if not isinstance(value, list):
		value = [value]
	bus.write_i2c_block_data(i2c_addr, reg_addr, value)

def deInit():
	i = 0;
	values = []
	while i < 18:
		values.append(0x00);
		i = i + 1
	update_leds(values)


bus = SMBus(i2c_bus)
write_i2c(CMD_ENABLE_OUTPUT, 0x01)
write_i2c(CMD_ENABLE_LEDS, [0xFF, 0xFF, 0xFF])
