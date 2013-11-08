# Python module for piglow peripheral for RaspberryPi.
# Initializes device, provides helper function.AInitialization
# code taken from pimoroni's example script

from smbus import SMBus

# command register addresses for SN3218 IC
CMD_ENABLE_OUTPUT = 0x00
CMD_ENABLE_LEDS = 0x13
CMD_SET_PWM_VALUES = 0x01
CMD_UPDATE = 0x16e

# TODO: Maybe this should go in a class __init__ member?
i2c_addr = 0x54 # i2c address of SN3218
i2c_bus = 1 # might be 0 on earliest Pi revisions?

def update_leds(values):
	print "update_leds() " + str(values)
	write_i2c(CMD_SET_PWM_VALUES, values)
	write_i2c(CMD_UPDATE, 0xFF)

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
