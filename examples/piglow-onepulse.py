#!/usr/bin/python2
#
# Example script for coydgoPiglow module. Soft pulse of LED's,
# one at a time.
import random
import time
import coydogPiglow

try:
	values = []
	i = 0
	while i < 18:
		values.append(0);
		i += 1
	bright = 255

        while True:
		done = False
		step = 1
		i = random.randrange(0,18)
		while not done:
			values[i] += step
			coydogPiglow.update_leds(values)

			if values[i] == bright:
				step = step * -1
			if step == -1 and values[i] == 0:
				done = True;

except KeyboardInterrupt:
	# set all the LEDs to "off" when Ctrl+C is pressed before exiting
	coydogPiglow.deInit()

