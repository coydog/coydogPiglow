#!/usr/bin/python2
#
# Example script for coydgoPiglow module. Soft pulse of all LED's,
# with randomization for an "organic" effect.
import random
import time
import coydogPiglow

try:
	values = []
	step = []
	i = 0
	while i < 18:
		values.append(0);
		step.append(1);
		i += 1
	bright = 127

        while True:
		i = random.randrange(0,18)
		#while i < len(values):
		values[i] += step[i]
			#i += 1
		if values[i] == 0 or values[i] == bright:
			step[i] = step[i] * -1

                # update the piglow with current values
                coydogPiglow.update_leds(values)
                
except KeyboardInterrupt:
	# set all the LEDs to "off" when Ctrl+C is pressed before exiting
	coydogPiglow.deInit()

