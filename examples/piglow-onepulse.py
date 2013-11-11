#!/usr/bin/python2
#
# Example script for coydgoPiglow module. Soft pulse of all LED's,
# with randomization for an "organic" effect.
import random
import time
import coydogPiglow
import sys

try:
	values = []
	i = 0
	while i < 18:
		values.append(0);
		i += 1
	bright = 255

        while True:
		done = False
		step_abs = 1
		if len(sys.argv) > 1:
			step_abs = int(sys.argv[1])
		if step_abs < 1:
			step_abs = 1
		step = step_abs
		i = random.randrange(0,18)
		while not done:
			values[i] += step
			coydogPiglow.update_leds(values)

			if values[i] >= bright:
				step = step * -1
			if step < 0  and values[i] <= 0:
				done = True;

except KeyboardInterrupt:
	# set all the LEDs to "off" when Ctrl+C is pressed before exiting
	coydogPiglow.deInit()

