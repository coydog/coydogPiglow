#!/usr/bin/python2
#
# Example script for coydgoPiglow module. Soft pulse of all LED's.
import random
import time
import coydogPiglow

try:
	values = []
	i = 0
	while i < 18:
		values.append(0);
		i += 1
	bright = 127
	step = 1

        while True:
		i = 0
		while i < len(values):
			values[i] += step
			i += 1
		if values[0] == 0 or values[0] == bright:
			step = step * -1

                # update the piglow with current values
                coydogPiglow.update_leds(values)
                time.sleep(.006)
                
except KeyboardInterrupt:
	# set all the LEDs to "off" when Ctrl+C is pressed before exiting
	coydogPiglow.deInit()

